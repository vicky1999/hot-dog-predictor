from flask import Flask,render_template,request
import tensorflow as tf
import numpy as np
import pandas as pd

# model=tf.keras.models.load_model('model/trained_model')

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def init():
    return render_template('index.html')

@app.route('/predict',methods=['GET','POST'])
def extract():
    if(request.method == 'POST'):
        print(request.files)
        f = request.files['image']
        f.save(secure_filename(f.filename))
        print(type(f))
        return 'file uploaded successfully'


if(__name__=='__main__'):
    app.run(host='0.0.0.0',port=5555,debug=True)