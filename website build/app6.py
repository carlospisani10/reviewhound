import os
import io
import base64
from flask import Flask, render_template, request
import os
import pandas as pd
import json 
import numpy as np
import keras.models
import re
import sys
sys.path.append(os.path.abspath("./Sentiment_Model"))
#from load import *
import logging
from keras.preprocessing import sequence
from keras.preprocessing.text import text_to_word_sequence
from keras.models import Sequential
from keras.layers import MaxPooling1D, Conv1D, Flatten, Dropout, Dense
from keras.layers.embeddings import Embedding
from keras.preprocessing import sequence
import tensorflow as tf

import keras
from keras.preprocessing import image
from keras.preprocessing.image import img_to_array
from keras import backend as K

from flask import Flask, request, redirect, jsonify, render_template

app = Flask(__name__)
model = None
graph = None

PATH = './Sentiment_Model/optimal_dict3.json'
with open(PATH) as json_data:
    d = json.load(json_data)
word_dict = pd.Series(d)

# Parameters
version = 4
words = len(word_dict)
review_len = 1000
vec_len = 300
patience = 5
batch_size = 40
epochs = 3

def load_model():
    global model
    global graph
    model = keras.models.load_model("./Sentiment_Model/optimalfloyds3.h5")
    graph = K.get_session().graph

load_model()

#econding functions
def encode_sentence(text):
    result = []
    arr = text_to_word_sequence(text, lower=True, split=" ")
    for word in arr:
        w = encode_word(word)
        if w is not None:
            result.append(w)
    return result

def encode_word(word):
    if word not in word_dict:
        return None
    return word_dict[word]

def encode_batch(arr):
    result = []
    for sentence in arr:
        result.append(encode_sentence(sentence))
    return sequence.pad_sequences(result, maxlen=review_len)

def predict_batch(arr):
    batch = encode_batch(arr)
    result = model.predict(batch, batch_size=len(batch), verbose=0)
    return result


app = Flask(__name__)

@app.route('/')
def index():
    return render_template("sniffer3.html")

@app.route('/prediction', methods=['GET', 'POST'],)
def predict():
    data = {"success": False}
    if request.method == 'POST':
        # read the base64 encoded string
        # review = request.form.get('userInput')
        review =  request.form['userInput'];

        # Get the tensorflow default graph
        global graph
        with graph.as_default():

            # Use the model to make a prediction

            # prediction = predict_batch(review)
            predictions = predict_batch([review])
            # data["prediction"] = str(prediction)
            data["review"] = review
            data["predictions"] = str(predictions)

            # indicate that the request was a success
            data["success"] = True
    return jsonify(data)

if __name__ == "__main__":
    load_model()
    app.run()