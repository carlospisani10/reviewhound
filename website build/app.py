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
from keras.callbacks import EarlyStopping
# from keras.datasets import imdb


# init flask app
app = Flask(__name__)

# global variables
#global model
#model = init()

# model importing
#load bag of words
PATH = './Sentiment_Model/optimal_dict3.json'
with open(PATH) as json_data:
    d = json.load(json_data)
word_dict = pd.Series(d)

#load model function
def build_model(words, vec_len, review_len):
    model = Sequential()
    model.add(Embedding(words, vec_len, input_length=review_len))
    model.add(Dropout(0.25))
    model.add(Conv1D(32, 3, padding="same"))
    model.add(MaxPooling1D(pool_size=2))
    model.add(Conv1D(16, 3, padding="same"))
    model.add(Flatten())
    model.add(Dropout(0.25))
    model.add(Dense(100, activation="sigmoid"))
    model.add(Dropout(0.25))
    model.add(Dense(1, activation="sigmoid"))
    model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])
    # model.summary()
    return model

# Parameters
version = 4
words = len(word_dict)
review_len = 1000
vec_len = 300
patience = 5
batch_size = 40
epochs = 3

# Build model
model = build_model(words, vec_len, review_len)

 # Model
from keras.preprocessing import sequence
from keras.models import load_model
model = load_model(("./Sentiment_Model/optimalfloyds3.h5"))

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


# app routes
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/index.html')
def indexNavigation():
    return render_template("index.html")


@app.route("/about.html")
def about():
    return render_template("about.html")


@app.route("/sniffer.html")
def sniffer():
    return render_template("sniffer.html")

@app.route('/sniffer/<user_input>', methods=['GET', 'POST'])
def predict(user_input):
    response = encode_batch(user_input)
    score = response[0][0]
    return score
    
    

# @app.route('/submitted', methods=['POST'])
# def submitted_form():
#     name = request.form['Carlos Guevara']
#     email = request.form['guevara.t.carlos@gmail.com']
#     ####idk what these are for
#     site = request.form['site_url']
#     comments = request.form['comments']

# @app.errorhandler(500)
# def server_error(e):
#     # log error and stacktrace
#     logging.exception('An error occured during a request.')
#     return 'An internal error occured.', 500
# # Heroku Mode

print(predict_batch([
"yes",
"good",
"this is the best thing ever",
"nice",
"bad",
"such a horrible judgement",
"no",
"shitty"
]))

if __name__ == "__main__":
    
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)