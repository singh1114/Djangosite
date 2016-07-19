from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Cement(models.Model):
	Company_Name = models.CharField("Name of the Company", max_length = 30)

	pc_type = (
		('OPC', 'OPC'),
		('PPC', 'PPC'),
	)

	grade = (
		('33', '33'),
		('43', '43'),
		('53', '53'),
	)

	Type_of_Cement = models.CharField(choices = pc_type, max_length = 9, default = "OPC")

	Grade_of_Cement = models.CharField(choices = grade, max_length = 9, default = "33")

	Price_of_Cement = models.FloatField("Price per 50kg.")	#Please change this name to price of cement.

	def __str__(self):
		return self.Company_Name

class BrickOrTile(models.Model):
	grade_of_brick = (
		('Grade I',' Grade I'),
		('Grade II',' Grade II'),
		('Grade III',' Grade III')
	)

	brick_or_tile = (
		('Brick', 'Brick'),
		('Tiles', 'Tiles')
	)

	Brand_of_Brick = models.CharField("Brands Available", max_length=30)

	Brick_or_Tiles = models.CharField(choices = brick_or_tile, max_length = 10, default = 'Brick')

	Grade_of_Brick = models.CharField(choices = grade_of_brick, max_length = 10, default = 'Grade I')

	Price_of_Brick = models.FloatField("Price of Brick or Tile per piece")

	def __str__(self):
		return self.Brand_of_Brick

class WaterTanker(models.Model):
	capacity_of_tanker = (
		('5000','5000'),
		('10000','10000')
	)

	Company_of_tanker = models.CharField("Company of tanker", max_length = 30)

	Capacity_of_Tanker = models.CharField("Capacity in litres", choices = capacity_of_tanker, max_length = 5)

	Price_of_Tanker = models.FloatField("Price of Tanker")

	def __str__(self):
		return self.Company_of_tanker


class Sand(models.Model):
	type_of_sand = (
		('course','Course'),
		('fine','Fine')
	)

	Type_of_Sand = models.CharField("Type of Sand", choices = type_of_sand, max_length = 30)

	Price_of_Sand = models.FloatField("Price of Sand")

	def __str__(self):
		return self.Type_of_Sand

class CourseAggregate(models.Model):
	place = (
		('Anandpur_Sahib', 'Anandpur Sahib'),
		('Pathankot', 'Pathankot'),
	)
	size = (
		('10', '10 mm'),
		('20', '20 mm'),
		('30', '30 mm'),
	)
	amount = (
		('100', '100 foot cube'),
		('250', '250 foot cube'),
		('1000', '1000 foot cube'),
	)
	Place_of_course = models.CharField("Place of Import", choices = place, max_length = 15)
	Size_of_course = models.CharField("Size of course", choices = size, max_length = 5)
	Amount_of_course = models.CharField("Choose a unit", choices = amount, max_length = 15)

	Price_of_Course = models.FloatField("Price of Course", default = 200)
	
	def __str__(self):
		return self.Place_of_course

