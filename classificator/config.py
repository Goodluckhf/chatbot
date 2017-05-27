import sys
from pathlib import Path # if you haven't already done so
root = str(Path(__file__).resolve().parents[1])

def getParams():
	return {
		'max_features' : 2279,
		'maxlen' : 151,
		'batch_size' : 10,
		'embedding_dims' : 100,
		'filters' : 200,
		'kernel_size' : 5,
		'hidden_dims' : 100,
		'epochs' : 10,
		'model_dict': root + '/classificator/tokenDictionary.npy',
		'first_model': root + '/classificator/myModel.h5',
		'second_model': root + '/myModel_1.h5',
		'thirty_model':'',
		'corpus': root + '/classificator/NEW_DATA.json'
	}