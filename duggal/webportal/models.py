from __future__ import unicode_literals

from django.db import models

# id field to add into every table..I am creating this field so that I can use this in the cart table(maybe).
class Idishere(models.Model):
	ids = models.AutoField(primary_key=True, blank=True, editable=False)

# Create your models here.
class Cement(Idishere):
	Company_Name = models.CharField("Name of the Company", max_length = 30, name="Company_Name")

	pc_type = (
		('OPC', 'OPC'),
		('PPC', 'PPC'),
	)

	grade = (
		('33', '33'),
		('44', '43'),
		('55', '53'),
	)

	Type_of_Cement = models.CharField(choices = pc_type, max_length = 9, default = "OPC")

	Grade_of_Cement = models.CharField(choices = grade, max_length = 9, default = "33")

	Price = models.FloatField("Price per 50kg.")	#Please change this name to price of cement.

	def __str__(self):
		return self.Company_Name


class BrickOrTile(Idishere):
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

	Price = models.FloatField("Price of Brick or Tile per piece")

	def __str__(self):
		return self.Brand_of_Brick

class WaterTanker(Idishere):
	capacity_of_tanker = (
		('5000','5000'),
		('10000','10000')
	)

	Company_of_tanker = models.CharField("Company of tanker", max_length = 30)

	Capacity_of_Tanker = models.CharField("Capacity in litres", choices = capacity_of_tanker, max_length = 10)

	Price = models.FloatField("Price of Tanker")

	def __str__(self):
		return self.Company_of_tanker


class Sand(Idishere):
	type_of_sand = (
		('Course','Course'),
		('Fine','Fine')
	)

	Type_of_Sand = models.CharField("Type of Sand", choices = type_of_sand, max_length = 30)

	Price = models.FloatField("Price of Sand")

	def __str__(self):
		return self.Type_of_Sand

class CourseAggregate(Idishere):
	place = (
		('Anandpur Sahib', 'Anandpur Sahib'),
		('Pathankot', 'Pathankot'),
	)
	size = (
		('10 mm', '10 mm'),
		('20 mm', '20 mm'),
		('30 mm', '30 mm'),
	)
	amount = (
		('100 cubic foot', '100 cubic foot'),
		('250 cubic foot', '250 cubic foot'),
		('1000 cubic foot', '1000 cubic foot'),
	)
	Place_of_course = models.CharField("Place of Import", choices = place, max_length = 15)
	Size_of_course = models.CharField("Size of course", choices = size, max_length = 10)
	Amount_of_course = models.CharField("Choose a unit", choices = amount, max_length = 15)
	Price = models.FloatField("Price of Course", default = 200)

	def __str__(self):
		return self.Place_of_course

class Cart(models.Model):
	product_id = models.IntegerField()
	product_name = models.CharField(max_length = 30)
	Quantity = models.CharField(max_length = 15)
	Amount = models.CharField(max_length = 10)
	userName = models.CharField(max_length = 30)

	def __str__(self):
		return self.Quantity
