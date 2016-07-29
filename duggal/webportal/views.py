from django.shortcuts import render

from django.http import HttpResponse

from .forms import cementform

from .models import *
# Create your views here.

def index(request):
    return render(request, 'webportal/index.html', {})

def cement(request):
	allcompanies = Cement.objects.all()
	grade = Cement.grade
	pc_type = Cement.pc_type

	context = {
		'allcompanies': allcompanies,
		'grade': grade,
		'pc_type': pc_type
	}


	return render(request, 'webportal/cement.html', context)

def cementicform(request):
	form = cementform(request.POST or None)
	context = {
		"form" : form
	}

	return render(request, "webportal/forms.html", context)

def output(request):
	query1 = request.POST.get('company_name')
	return HttpResponse(query1)