from django import forms
from .models import *


class cementform(forms.Form):
	grade = Cement.grade
	#print(grade)
	temp = Cement.objects.order_by().values('Company_Name').distinct()
	temp5 = Cement.objects.order_by().values('id').distinct()
	#print(temp)
	temp2 =()
	temp3 = 0
	for temp1 in temp:
		temp2 = ((temp5[temp3]['id'], temp1['Company_Name']),) + temp2
		temp3 = temp3+1

	print(temp2)
	companies_name = Cement.objects.all()
	# loop to create a variable with different choices at list key
	companies_name = tuple(companies_name)
	print(companies_name)
	x = 0
	z = ()
	for q in companies_name:
		z=((q.id, q.Company_Name),)+z
		x = x+1

	print(z)
	z = tuple(z)

	#companies_name = companies_name.Company_Name
	company_name = forms.ChoiceField(choices=temp2)
	Type = forms.CharField()
	Grade = forms.CharField()
	bag_numbers = forms.IntegerField()
	print(company_name)


