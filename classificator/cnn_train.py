#coding: utf-8

'''
КЛАССЫ:
0 - Беседа
1 - Контакты
2 - Форма запроса
3 - Доставка
'''
from __future__ import print_function
import json
import numpy as np
import codecs
import config
import model
import helpers
import predictor
from sklearn import metrics
from keras.preprocessing import sequence

x_train = []
y_train = []

x_test = []
y_test = []

tokens = []
params = config.getParams()

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
    tokens = helpers.tokenizer(text.lower())    
    unique_tokens = set(tokens); 
    print('tokens length: ', len(unique_tokens))
    #exit()
    i = 1
    dictionary['unknown'] = 0                   
    for item in unique_tokens:
        dictionary[item] = i
        i +=1  
    for record in dataset:
        tokenize = helpers.tokenizer(record['text'])
        temp = []
        for item in tokenize:
            temp.append(dictionary[item.lower()])    
        x_train.append(temp)
    np.save('tokenDictionary',dictionary)    
    return(x_train,y_train)
        
jsonfile = codecs.open( params['corpus'], 'r', 'utf_8_sig')
data = json.loads(jsonfile.read())
test_data = (x_test,y_test)
x_train,y_train = prepare_data(data)
# set parameters:

print('Loading data...')
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

print(metrics.f1_score(y_test,predictor.predict_list(y_test)))