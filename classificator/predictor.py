# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 20:55:55 2017

@author: Никита
"""
#coding: utf-8
from __future__ import print_function
import json
import numpy as np
from keras.preprocessing import sequence
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.layers import Embedding
from keras.layers import Conv1D, GlobalMaxPooling1D
from nltk.tokenize import word_tokenize
from keras.datasets import imdb

max_features = 2186
maxlen = 151
batch_size = 10
embedding_dims = 100
filters = 200
kernel_size = 5
hidden_dims = 250
epochs = 10

model = Sequential()

# we start off with an efficient embedding layer which maps
# our vocab indices into embedding_dims dimensions
model.add(Embedding(max_features,
                    embedding_dims,
                    input_length=maxlen))
model.add(Dropout(0.2))

# we add a Convolution1D, which will learn filters
# word group filters of size filter_length:
model.add(Conv1D(filters,
                 kernel_size,
                 padding='valid',
                 activation='relu',
                 strides=1))
# we use max pooling:
model.add(GlobalMaxPooling1D())

# We add a vanilla hidden layer:
model.add(Dense(hidden_dims))
model.add(Dropout(0.2))
model.add(Activation('relu'))

# We project onto a single unit output layer, and squash it with a sigmoid:
model.add(Dense(4))
model.add(Activation('softmax'))
model.load_weights('myModel.h5')
model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

read_dictionary = np.load('tokenDictionary.npy').item()


def getNameByPred(pred):
    label = np.argmax(pred)
    print(pred)
    if label == 0:
        return "Беседа"
    if label == 1:
        return "Контактная информация"
    if label == 2:
        return "Форма запроса"
    if label == 3:
        return "Информация по доставке"
        

def tokenizer(text):
    result = text
    result = result.replace('.', ' . ')
    result = result.replace(' . . . ', ' ... ')
    result = result.replace(',', ' , ')
    result = result.replace(':', ' : ')
    result = result.replace(';', ' ; ')
    result = result.replace('!', ' ! ')
    result = result.replace('?', ' ? ')
    result = result.replace('\"', ' \" ')
    result = result.replace('\'', ' \' ')
    result = result.replace('(', ' ( ')
    result = result.replace(')', ' ) ') 
    result = result.replace(' ', ' ')
    result = result.replace(' ', ' ')
    result = result.replace(' ', ' ')
    result = result.replace(' ', ' ')
    result = result.replace('^', ' ^ ')
    result = result.strip()
    result = result.split(' ')
    return result


def predict(text_input):
    tokenize = tokenizer(text_input)
    temp = np.zeros((1, maxlen), dtype=np.integer)
    for t, item in enumerate(tokenize):
        if item.lower() in read_dictionary:
            temp[0, t] = read_dictionary[item.lower()]
        else:
            temp[0, t] = 0
    
    test = model.predict(temp)[0]
    return test
    
    