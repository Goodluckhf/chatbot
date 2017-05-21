from __future__ import print_function
import json
import numpy as np
import codecs
import config
import extra_metrics
from sklearn import metrics
from keras.preprocessing import sequence
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.layers import Embedding
from keras.layers import Conv1D, GlobalMaxPooling1D
import gc;

params = config.getParams()

def getModel():
	model = Sequential()

	#input layer
	model.add(Embedding(params['max_features'],
	                    params['embedding_dims'],
	                    input_length=params['maxlen']))
	model.add(Dropout(0.2))

	#convlution layer 1D
	model.add(Conv1D(params['filters'],
	                 params['kernel_size'],
	                 padding='valid',
	                 activation='relu',
	                 strides=1))
	# we use max pooling:
	model.add(GlobalMaxPooling1D())

	#  hidden layer:
	model.add(Dense(params['hidden_dims']))
	model.add(Dropout(0.2))
	model.add(Activation('relu'))

	#output layer:
	model.add(Dense(4))
	model.add(Activation('softmax'))

	return model

#def f1_score(tags, predicted):
#
#   tags = set(tags)
#    predicted = set(predicted)

#    tp = len(tags & predicted)
#    fp = len(predicted) - tp 
#    fn = len(tags) - tp

#    if tp>0:
#        precision=float(tp)/(tp+fp)
#        recall=float(tp)/(tp+fn)
#        return 2*((precision*recall)/(precision+recall))
#    else:
#        return 0


def getModelForTrain(x_train, y_train):
	model = getModel()

	model.compile(
		loss='categorical_crossentropy',
		optimizer='adam',
		metrics=[extra_metrics.fmeasure,'accuracy']
	)

	return model

def fit(x_train, y_train):
	model = getModelForTrain(x_train, y_train)
	model.fit(
		x_train,
		y_train,
		batch_size=params['batch_size'],
		epochs=params['epochs'],
	)
	gc.collect()
	return model	

def getFitted(filename):
	model = getModel()
	model.load_weights(filename) #in current directory
	model.compile(
		loss='categorical_crossentropy',
		optimizer='adam',
		metrics=['accuracy']
	)

	return model