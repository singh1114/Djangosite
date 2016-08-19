from django import forms
from .models import *
from .views import *

# class to create the tuple for taking values from the models
class creatingtuple:

	def __init__(self, modelname, fieldname):
		self.modelname = modelname
	  	self.fieldname = fieldname

	def onefunction(self):
		thismodel = self.modelname
		distcompanyname = thismodel.objects.order_by().values(self.fieldname).distinct()	
		companynametuple =()
		tempvar1 = 0
		for tempvar2 in distcompanyname:
			companynametuple = ((tempvar2[self.fieldname], tempvar2[self.fieldname]),) + companynametuple
			tempvar1 = tempvar1 + 1

		return companynametuple

class cementform(forms.Form):
	#Code to show all the dinstict companies name as choices
	# simple variable store the company name
	modelname = Cement	
	fieldname = "Company_Name"
	pro = creatingtuple(modelname, fieldname)

	#code to create the real forms
	Company_Name = forms.ChoiceField(choices=pro.onefunction())
	Type = forms.ChoiceField(choices=Cement.pc_type)
	Grade = forms.ChoiceField(choices=Cement.grade)
	Total_Quantity = forms.IntegerField()

class courseform(forms.Form):
	# creating form and choices, show them in forms
	Place_of_Import = forms.ChoiceField(choices=CourseAggregate.place)
	Size_of_Course = forms.ChoiceField(choices=CourseAggregate.size)
	Quantity_of_Course = forms.ChoiceField(choices=CourseAggregate.amount)
	Total_Quantity = forms.IntegerField()

class brickform(forms.Form):
	modelname = BrickOrTile	
	fieldname = "Brand_of_Brick"
	pro = creatingtuple(modelname, fieldname)

	Companies_Available = forms.ChoiceField(choices=pro.onefunction())
	Brick_or_Tile = forms.ChoiceField(choices=BrickOrTile.brick_or_tile)
	Grade = forms.ChoiceField(choices=BrickOrTile.grade_of_brick)
	Total_Quantity = forms.IntegerField()

class tankerform(forms.Form):
	modelname = WaterTanker
	fieldname = "Company_of_tanker"
	pro = creatingtuple(modelname, fieldname)
	# creating form and choices, show them in forms
	Company_of_tanker = forms.ChoiceField(choices=pro.onefunction())
	Capacity_of_tanker = forms.ChoiceField(choices=WaterTanker.capacity_of_tanker)
	Total_Quantity = forms.IntegerField()

class sandform(forms.Form):
	# creating form and choices, show them in forms
	Type_of_sand = forms.ChoiceField(choices=Sand.type_of_sand)
	Total_Quantity = forms.IntegerField()
