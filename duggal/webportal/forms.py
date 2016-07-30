from django import forms
from .models import *


class cementform(forms.Form):
	grade = Cement.grade
	print(grade)
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

	for h in companies_name:
		m = ()
		if(h.Company_Name != m.Company_Name):
			m =((h),) + m

		print(h)
	#companies_name = companies_name.Company_Name
	company_name = forms.ChoiceField(choices=z)
	Type = forms.CharField()
	Grade = forms.CharField()
	bag_numbers = forms.IntegerField()


