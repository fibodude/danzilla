from django.db import models

# Create your models here.


class Level(models.Model):
	name = models.CharField(max_length=100)
	author = models.CharField(max_length=100)
	data = models.TextField()
