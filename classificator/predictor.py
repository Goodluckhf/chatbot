# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 20:55:55 2017

@author: Никита
"""
#coding: utf-8
from __future__ import print_function
import json
import numpy as np
import sys
from pathlib import Path # if you haven't already done so
root = str(Path(__file__).resolve().parents[1])
sys.path.append(root)
from classificator import config
from classificator import model
from classificator import helpers
'''
КЛАССЫ:
0 - Беседа
1 - Контакты
2 - Форма запроса
3 - Доставка
'''

config = config.getParams()

def predict(text_input,model_name):
    read_dictionary = np.load(config['model_dict']).item()
    model1 = model.getFitted(config[model_name])
    tokenize = helpers.tokenizer(text_input)
    temp = np.zeros((1, config['maxlen']), dtype=np.integer)
    for t, item in enumerate(tokenize):
        if item.lower() in read_dictionary:
            temp[0, t] = read_dictionary[item.lower()]
        else:
            temp[0, t] = 0
    
    test = model1.predict(temp)[0]
    return test
    
def predict_list(test_list,model_name):
    model2 = model.getFitted(config[model_name])
    print('list', test_list);
    test = model2.predict(test_list)
    return test