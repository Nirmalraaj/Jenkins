from flask import Flask
#import os
#import datetime
#import requests
#import awscli
#import botocore
import boto3
#import mutagen

#import  werkzeug
import sys
#import pillow
app = Flask(__name__)
@app.route("/")
def hello():
   return "Hello from Python!"
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=5000)
