import random
import re


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
			'type': 'Память',
			'question': [
				"Сколько памяти вам нужно?",
				"Какой объем памяти вы хотите?"
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
		import sys
		from pathlib import Path
		root = str(Path(__file__).resolve().parents[1])
		sys.path.append(root)
		from chatbot_interface.models import Phone

		allAnswer = "Вы хотите телефон с такими характиристиками: <br>"
		for i, elem in enumerate(self.answers):
			allAnswer += FormRequest.questions[elem - 1]['type'] + ": " + self.answers[elem] + "; <br>"
		try:
			print("Цена >>>>", self.getDigits(self.answers[2]))
			print("Память >>>>", self.getDigits(self.answers[3]))
			print("Цвет >>>>", self.answers[1])
			phone = Phone.objects.filter(
				price__lt  = self.getDigits(self.answers[2]),
				memory__gt = self.getDigits(self.answers[3]),
				color      = self.answers[1]
			).order_by("?").first()
		except Phone.DoesNotExist:
			return allAnswer + "<br> <span style='color:tomato'>По вашему запрому ничего не найдено!</span>"
		if not phone:
			return allAnswer + "<br> <span style='color:tomato'>По вашему запрому ничего не найдено!</span>"
		
		return allAnswer + "Вот что я нашел:<br> <span class='title'>" + phone.title + "</span><img src='/static" + phone.image + "'><span class='price'>Цена: " + str(phone.price) + " Рублей.</span>"

	def getDigits(self, sentence):
		regexp = re.compile(r'\d+')
		return regexp.findall(sentence)[0]
