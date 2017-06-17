import sys
from pathlib import Path # if you haven't already done so
root = str(Path(__file__).resolve().parents[1])
sys.path.append(root)
from classificator.predictor import Predictor as ClassificatorPredictor
import numpy as np


classificator = ClassificatorPredictor('second_model')

def getNameByPred(pred):
    label = np.argmax(pred)
    print(pred)
    if label == 0:
        return "Беседа"
    if label == 1:
        return "Контактная информация"
    if label == 2:
        return "Форма запроса"
    if label == 3:
        return "Информация по доставке"
        
def chat_loop():
    while True:
        user_input = str(input(">>>>>").lower().strip())
        output = getNameByPred(classificator.predict(user_input))
        print(output)

if __name__ == "__main__":
    chat_loop()