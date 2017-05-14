import predictor
import numpy as np

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
        output = getNameByPred(predictor.predict(user_input))
        print(output)

if __name__ == "__main__":
    chat_loop()