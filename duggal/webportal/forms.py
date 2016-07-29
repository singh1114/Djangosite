from django import forms
from .models import *


class cementform(forms.Form):
	grade = Cement.grade
	company_name = forms.ChoiceField(choices=grade)
	Type = forms.CharField()
	Grade = forms.CharField()
	bag_numbers = forms.IntegerField()


