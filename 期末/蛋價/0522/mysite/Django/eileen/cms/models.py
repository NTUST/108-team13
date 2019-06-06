from __future__ import unicode_literals
from django.db import models

# Create your models here.

class egg(models.Model):
	kind = models.CharField(max_length=20)
	price = models.CharField(max_length=15)
	region = models.CharField(max_length=50)

	def __str__(self):
		return self.kind
