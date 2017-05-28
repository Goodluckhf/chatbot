import random

class FormRequest:

	questions = {
		0: {
			'type': "Цвет",
			'question': [
				"Какого цвета вы хотите телефон?",
				"Подскажите цвет, который вы хотите?",
				"Какое предпочтение по цвету?"
			]
		},
		1: {
			'type': "Цена",
			'question': [
				"Какую максимальную цену вы готовы заплатить?",
				"Сколько вы готовы заплатить за телефон?",
				"За сколько вы готовы купить телефон"
			]
		},
		2: {
			'type': 'Разрешение',
			'question': [
				"Какое разрешение экрана вы хотите?",
				"Скажите ваше предпочтение по разрешению экрана"
			]
		} 
	}

	def __init__(self):
		self.questionNumber = 0
		self.answers = {}

	def isResultNeed(self):
		return len(FormRequest.questions) == self.questionNumber

	def pickRandomQuestion(self):
		currentQuestions = FormRequest.questions[self.questionNumber]['question']
		randomQuestion = random.choice(currentQuestions)
		print(randomQuestion)
		return randomQuestion

	def setAnswer(self, answer):
		self.answers[self.questionNumber] = answer

	def getNextQuestion(self):
		if not self.isResultNeed():
			randomQuestion = self.pickRandomQuestion()
			self.questionNumber += 1
			return randomQuestion, False

		return self.getAllAnswers(), True

	def getAllAnswers(self):
		allAnswer = "Вы хотите телефон с такими характиристиками: <br>"
		for i, elem in enumerate(self.answers):
			allAnswer += FormRequest.questions[elem - 1]['type'] + ": " + self.answers[elem] + "; <br>"

		return allAnswer

