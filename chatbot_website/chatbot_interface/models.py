from django.db import models

# Create your models here.
class Phone(models.Model):
	title  = models.CharField(max_length=200)
	color  = models.CharField(max_length=100)
	memory = models.CharField(max_length=100)
	price  = models.FloatField()
	image  = models.CharField(max_length=200)