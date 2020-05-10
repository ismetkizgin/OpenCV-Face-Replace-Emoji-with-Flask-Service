# -*- coding: utf-8 -*-
"""
Created on Fri May  8 14:43:45 2020

@author: sefa
"""

from PIL import Image
import os
from flask import Flask, request,  send_file
from werkzeug.utils import secure_filename
import cv2
import numpy as np

UPLOAD_FOLDER = './images/'
ALLOWED_EXTENSIONS = set(['jpeg'])

face_cascade = cv2.CascadeClassifier('haarcascade-frontalface-default.xml')
app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):    
            filename = secure_filename(file.filename)
            print(filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            img = cv2.imread("images/"+filename) 
            img = detect(img)
            cv2.imwrite("images/"+filename,img)
            return send_file('images/' + file.filename, mimetype='image/jpg')
    

def detect(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, width, height) in faces:
        emoji = Image.open('emoji.png')
        emoji = emoji.resize((width, height), Image.LANCZOS)
        pilim = Image.fromarray(frame)
        pilim.paste(emoji,box=(x,y),mask=emoji)
        frame = np.array(pilim)
    return frame

if __name__ == '__main__':
    app.run(port=5000,debug=True)


