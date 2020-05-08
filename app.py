# -*- coding: utf-8 -*-
"""
Created on Fri May  8 14:43:45 2020

@author: sefa
"""

from PIL import Image
from flask import Flask,jsonify,request
import cv2
import numpy as np
import base64
import io



face_cascade = cv2.CascadeClassifier('haarcascade-frontalface-default.xml')
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"



@app.route('/', methods=['POST']) 
def foo():
    data = request.json
    imgdata = base64.b64decode(str(data["imageCode"]))
    image = Image.open(io.BytesIO(imgdata))
    print(type(image))
    
    
    
    
    return jsonify(data)
    



    
    
    


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


