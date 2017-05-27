import sys
from pathlib import Path # if you haven't already done so
path_file = Path(__file__)
root = str(path_file.resolve().parents[1])
print(Path(root).joinpath('classificator/myModel.h5'))

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
		'model_dict': str(Path(root).joinpath('classificator/tokenDictionary.npy')),
		'first_model':str(Path(root).joinpath('classificator/myModel.h5')),
		'second_model':str(Path(root).joinpath('classificator/myModel_1.h5')),
		'thirty_model':'',
		'corpus': str(Path(root).joinpath('classificator/NEW_DATA.json'))
	}