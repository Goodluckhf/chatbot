'''This example demonstrates the use of Convolution1D for text classification.

Gets to 0.89 test accuracy after 2 epochs.
90s/epoch on Intel i5 2.4Ghz CPU.
10s/epoch on Tesla K40 GPU.

КЛАССЫ:
0 - Беседа
1 - Контакты
2 - Форма запроса
3 - Доставка
'''
#coding: utf-8
from __future__ import print_function
import json
import numpy as np
import codecs
import config
import model
from keras.preprocessing import sequence
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.layers import Embedding
from keras.layers import Conv1D, GlobalMaxPooling1D
from nltk.tokenize import word_tokenize

x_train = []
y_train = []

x_test = []
y_test = []

tokens = []

params = config.getParams()

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

def print_array(array):
    for item in array:
        print(item)

def class_to_binary(status):
    if status == '0':
        return [1,0,0,0]
    if status == '1':
        return [0,1,0,0]
    if status == '2':
        return [0,0,1,0]
    if status == '3':
        return [0,0,0,1]

def prepare_data(dataset):
    dictionary = dict()
    text = ""
#    maxlen = 0
    for record in dataset:
#        if len(record['text']) > maxlen:
#           maxlen = len(record['text'])
        text += record['text']+" "
        y_train.append(class_to_binary(record['status']))    
    tokens = tokenizer(text.lower())    
    unique_tokens = set(tokens);                   
    i = 1
    dictionary['unknown'] = 0                   
    for item in unique_tokens:
        dictionary[item] = i
        i +=1  
    for record in dataset:
        tokenize = tokenizer(record['text'])
        temp = []
        for item in tokenize:
            temp.append(dictionary[item.lower()])    
        x_train.append(temp)
    np.save('tokenDictionary',dictionary)    
    return(x_train,y_train)
        
        

#f = open('D:\toolkits\data.json','r')
jsonfile = codecs.open( 'D:\\toolkits\\NEW_DATA.json', 'r', 'utf_8_sig')
data = json.loads(jsonfile.read())
test_data = (x_test,y_test)
x_train,y_train = prepare_data(data)
# set parameters:

print('Loading data...')
#(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=max_features)



print(len(x_train), 'train sequences')
print(len(x_test), 'test sequences')

print('Pad sequences (samples x time)')
x_train = sequence.pad_sequences(x_train, maxlen=params['maxlen'])
x_test = sequence.pad_sequences(x_test, maxlen=params['maxlen'])


print('x_train shape:', x_train.shape)
print('x_test shape:', x_test.shape)

print('Build model...')
model = model.fit(x_train,y_train)

model.save_weights('myModel.h5',overwrite=True)