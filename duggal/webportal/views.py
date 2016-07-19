from django.shortcuts import render

from .models import Cement
# Create your views here.

def product_list(request):
    return render(request, 'webportal/index.html', {})

