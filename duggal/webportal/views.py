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
	query1 = request.POST.get('company_Name')
	query2 = request.POST.get('Type')
	query3 = request.POST.get('Grade')
	query4 = request.POST.get('Number_of_Bags')
	x = Cement.objects.filter(Company_Name = query1, Type_of_Cement = query2, Grade_of_Cement = query3)
	
	for m in x:
		z = m.Price_of_Cement

	#we can only return string as httpresponse so this is changed to string
	totalprice = str(z*float(query4))
	
	request.session['quantity'] = query4
	request.session['itemName'] = "Cement"
	request.session['totalprice'] = totalprice

	context = {
		"query1" : query1,
		"query2" : query2,
		"query3" : query3,
		"query4" : query4,
		"totalprice" : totalprice,
	}
	#return HttpResponse(query1+" "+query2+" "+query3+" "+totalprice)
	return render(request, "webportal/cementprice.html", context)

def input(request):
	itemName = request.session.get('itemName')
	quantity = request.session.get('quantity')
	totalprice = request.session.get('totalprice')
	x = cart(Item_Name=itemName, Quantity=quantity, Amount=totalprice)
	x.save()
	y = cart.objects.all()
	
	context = {
		"y": y,
	}	
	#return HttpResponse(z+" "+itemName+" "+quantity+" "+totalprice)
	return render(request, "webportal/cart.html", context)