from django import forms
from .models import *


class cementform(forms.Form):
	#Code to show all the dinstict companies name ass choices

	distcompanyname = Cement.objects.order_by().values('Company_Name').distinct()
	
	companynametuple =()
	tempvar1 = 0
	for tempvar2 in distcompanyname:
		companynametuple = ((tempvar2['Company_Name'], tempvar2['Company_Name']),) + companynametuple
		tempvar1 = tempvar1 + 1

	#code to write choices of types
	Type = Cement.pc_type

	#code to write choices of grades
	grade = Cement.grade

	#code to create the real forms
	company_name = forms.ChoiceField(choices=companynametuple)
	Type = forms.ChoiceField(choices=Type)
	Grade = forms.ChoiceField(choices=grade)
	bag_numbers = forms.IntegerField()


