from flask import Flask, render_template, request
import re
from bs4 import BeautifulSoup
import urllib3
#from werkzeug.utils import secure_filename
#from gevent.pywsgi import WSGIServer

app = Flask(__name__)
		
@app.route("/", methods = ["GET", "POST"])
def home():
	if request.method == "GET":
		return render_template("index.html")
	if request.method == "POST":
		text = request.form['textbox']
		product_name, price, img_url, pd = details(text)
		return render_template("after.html", product_name = product_name, price = price, img_url = img_url, pd = pd)


def details(url):
	http = urllib3.PoolManager()
	html_contents = http.request('GET', url).data
	soup = BeautifulSoup(html_contents, "html.parser")
	try:
		product_name = soup.find('span',id = "productTitle").text.rstrip().lstrip()
	except AttributeError:
		product_name = "N/A"
	try:
		price = soup.find('div', id = 'price')
		price = soup.find('span', id = re.compile('priceblock')).text
	except AttributeError:
		price = "N/A"
		
	try:
		pd = soup.find('ul', class_ = "a-unordered-list a-vertical a-spacing-mini").text #.replace('\n','')
	except AttributeError:
		pd = "N/A"
		
	try:
		img_url = soup.find('div', id = "imgTagWrapperId").find('img').attrs['src']
	except AttributeError:
		img_url = "N/A"
	return product_name, price, img_url, pd
	

if __name__ == "__main__":
	app.run(debug=True)
