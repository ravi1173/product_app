from flask import Flask, render_template, request
import backend
from werkzeug.utils import secure_filename
from gevent.pywsgi import WSGIServer

application = app = Flask(__name__)

@application.route("/", methods = ["GET", "POST"])
def home():
    if request.method == "GET":
        return render_template("index.html")
    if request.method == "POST":
        text = request.form.get('textbox')
        pn, price, pd, img_url = backend.get_details(text)
        return render_template("after.html", product_name = pn, price = price, pd = pd,img_url = img_url)

if __name__ == "__main__":
    application.run(debug=True)