import re
from bs4 import BeautifulSoup
import urllib3
from urllib.request import urlopen
#import urllib.request as urllib2

def get_details(url):
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
		pd = soup.find('div', id = "productDescription").text.replace('\n','')
	except AttributeError:
		pd = "N/A"
		
	try:
		img_url = soup.find('div', id = "imgTagWrapperId").find('img').attrs['src']
	except AttributeError:
		img_url = "N/A"
	
	
	return product_name, price, pd, img_url
	
