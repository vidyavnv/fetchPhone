from flask import Flask
from flask import request,jsonify
from flask import render_template
from createIndex import getPhoneDetails
import json

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template("phonedesc.html")

@app.route('/', methods=['POST'])
def my_form_post():

    text = request.form['text']
    details = getPhoneDetails(text)
    # phones = json.dumps(details)
    return jsonify(**details)

if __name__ == '__main__':
	app.debug = True
	app.run()