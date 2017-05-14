# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 20:55:55 2017

@author: Никита
"""
#coding: utf-8
from __future__ import print_function
import json
import numpy as np
import config
import model
import helpers

config = config.getParams()
model = model.getFitted(config['fitted_model'])
read_dictionary = np.load(config['model_dict']).item()

def predict(text_input):
    tokenize = helpers.tokenizer(text_input)
    temp = np.zeros((1, config['maxlen']), dtype=np.integer)
    for t, item in enumerate(tokenize):
        if item.lower() in read_dictionary:
            temp[0, t] = read_dictionary[item.lower()]
        else:
            temp[0, t] = 0
    
    test = model.predict(temp)[0]
    return test
    
    