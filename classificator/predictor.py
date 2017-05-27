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
import tensorflow as tf

'''
КЛАССЫ:
0 - Беседа
1 - Контакты
2 - Форма запроса
3 - Доставка
'''

config = config.getParams()
class Predictor:
    def __init__(self, model_name):
        self.model = model.getFitted(config[model_name])
        self.dict = np.load(config['model_dict']).item()
        self.graph = tf.get_default_graph()

    def predict(self, text_input):
        with self.graph.as_default():
            temp = np.zeros((1, config['maxlen']), dtype=np.integer)
            tokenizer = helpers.tokenizer(text_input)
            for t, item in enumerate(tokenizer):
                if item.lower() in self.dict:
                    temp[0, t] = self.dict[item.lower()]
                else:
                    temp[0, t] = 0
            
            test = self.model.predict(temp)[0]
            return test

    def predict_list(self, test_list):
        with self.graph.as_default():
            print('list', test_list);
            test = self.model.predict(test_list)
            return test