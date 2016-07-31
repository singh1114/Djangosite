from django.shortcuts import render

from django.http import HttpResponse

from .forms import cementform

from .models import *
# Create your views here.

def index(request):
    return render(request, 'webportal/index.html', {})

def cementicform(request):
	form = cementform(request.POST or None)
	context = {
		"form" : form
	}

	return render(request, "webportal/cement.html", context)

def output(request):
	query1 = request.POST.get('company_name')
	return HttpResponse(query1)
	print(query1)