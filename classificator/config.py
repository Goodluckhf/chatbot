def getParams():
	return {
		'max_features' : 2245,
		'maxlen' : 151,
		'batch_size' : 10,
		'embedding_dims' : 100,
		'filters' : 200,
		'kernel_size' : 5,
		'hidden_dims' : 250,
		'epochs' : 10,
		'model_dict': 'tokenDictionary.npy',
		'first_model': 'myModel.h5',
		'second_model': '',
		'thirty_model':'',
		'corpus': 'NEW_DATA.json'
	}