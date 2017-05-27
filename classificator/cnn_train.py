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
import sys
from pathlib import Path # if you haven't already done so
root = str(Path(__file__).resolve().parents[1])
sys.path.append(root)
from classificator import config
from classificator import model
from classificator import helpers
from classificator import predictor
from sklearn import metrics
from keras.preprocessing import sequence
import gc
gc.collect()

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
        if(int(record['id']) > 1587):
            text += record['text']+" "
            y_test.append(class_to_binary(record['status']))
        else:    
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
        if(int(record['id']) > 1587):
            tokenize = helpers.tokenizer(record['text'])
            temp1 = []
            for item in tokenize:
                temp1.append(dictionary[item.lower()])    
            x_test.append(temp1)
        else:   
            tokenize = helpers.tokenizer(record['text'])
            temp = []
            for item in tokenize:
                temp.append(dictionary[item.lower()])    
            x_train.append(temp)
    np.save('tokenDictionary',dictionary)    
    return(x_train,y_train,x_test,y_test)
        
jsonfile = codecs.open( params['corpus'], 'r', 'utf_8_sig')
data = json.loads(jsonfile.read())
test_data = (x_test,y_test)
x_train,y_train,x_test,y_test = prepare_data(data)

print('len(x_train) = ', len(x_train))
print('len(y_train) = ', len(y_train))
print('x_test = ', len(x_test))
print('len(y_test) = ' ,len(y_test))
#exit()


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
model.save_weights(params['second_model'],overwrite=True)

preds = predictor.predict_list(x_test,'second_model')
gc.collect()

