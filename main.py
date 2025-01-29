# Michael Niebauer
# Project 1
# Simple web application in python and flask to receive images and store them in the cloud.
# mniebaue@fau.edu
# 1/28/2025

import os
from flask import Flask, redirect, request, send_file
os.makedirs('files', exist_ok = True)

app = Flask(__name__)
@app.route('/')
def index():
    index_html="""
    <body style="background-color:grey">
    <br>
    <br>
    <H1>Upload Images to Google Cloud Storage</H1>
    <form method="post" enctype="multipart/form-data" action="/upload" method="post">
        <div>
            <label for="file">Choose file to upload</label>
            <input type="file" id="file" name="form_file" accept="image/jpeg"/>
        </div>
        <div>
            <button>Submit</button>
        </div>
    </form>
"""    
    for file in list_files():
       index_html += "<li><a href=\"/mount-folder/files/media/images/" + file + "\">" + file + "</a></li>"
    return index_html

@app.route('/upload', methods=["POST"])
def upload():
    file = request.files['form_file']  # item name must match name in HTML form
    file.save(os.path.join("./mount-folder/files/media/images", file.filename))
    return redirect("/")

@app.route('/mount-folder/files/media/images/')
def list_files():
 #   files = os.listdir("./files")
    files = os.listdir("./mount-folder/files/media/images/")
    jpegs = []
    for file in files:
        if file.lower().endswith(".jpeg") or file.lower().endswith(".jpg"):
            jpegs.append(file)
    return jpegs

@app.route('/mount-folder/files/media/images/<filename>')
def get_file(filename):
  return send_file('./mount-folder/files/media/images/'+ filename)
  #return send_file('./mount-folder/'+ filename)

if __name__ == '__main__':
    app.run(debug=True)
