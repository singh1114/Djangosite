from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Cement(models.Model):
	company_name = models.CharField("Name of the Company", max_length = 30)

	pc_type = (
		('OPC', 'OPC'),
		('PPC', 'PPC'),
	)

	grade = (
		('33', '33'),
		('43', '43'),
		('53', '53'),
	)

	Type = models.CharField(choices = pc_type, max_length = 9, default = "OPC")

	Grade = models.CharField(choices = grade, max_length = 9, default = "33")

	price = models.IntegerField("Price per 50kg.")	

	def __str__(self):
		return self.company_name

