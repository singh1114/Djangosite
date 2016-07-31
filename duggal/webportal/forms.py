from django import forms
from .models import *


class cementform(forms.Form):
	grade = Cement.grade
	#print(grade)
	distcompanyname = Cement.objects.order_by().values('Company_Name').distinct()
	ids = Cement.objects.order_by().values('id').distinct()
	#print(temp)
	companynametuple =()
	tempvar1 = 0
	for tempvar2 in distcompanyname:
		companynametuple = ((ids[tempvar1]['id'], tempvar2['Company_Name']),) + companynametuple
		tempvar1 = tempvar1 + 1

	print(companynametuple)
	

	#companies_name = companies_name.Company_Name
	company_name = forms.ChoiceField(choices=companynametuple)
	Type = forms.CharField()
	Grade = forms.CharField()
	bag_numbers = forms.IntegerField()
	print(company_name)


