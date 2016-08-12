from django.shortcuts import render

from django.http import HttpResponse

from .forms import cementform

from pprint import pprint

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

	for f in x:
		g = f.ids

	#we can only return string as httpresponse so this is changed to string
	totalprice = str(z*float(query4))
	
	request.session['quantity'] = query4
	request.session['totalprice'] = totalprice
	request.session['ids'] = g

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
	# get all the session variables into some local variables
	quantity = request.session.get('quantity')
	totalprice = request.session.get('totalprice')
	ids = request.session.get('ids')

	# Put them into the cart model/database
	x = cart(product_id=ids, Quantity=quantity, Amount=totalprice)
	x.save()

	d = 0
	f = cart.objects.all()
	w = []
	for a in f:
		b = a.product_id
		#print(b)
		w.insert(d, Cement.objects.filter(ids=b))
		d = d+1


	d = 0
	r = {}
	f = []
	#values = []
	#s = {}
	for e in w:
		r.update(vars(e[0]))
		f.insert(d, r)
		#values.insert(d,r[d].values())
		#s["items"] = vars(e[0])
		#s["values"] = r[d].values()
		#s.update(s)
		#s = s + {"items":vars(e[0]), "values":r[d].values()}
		d = d+1

	print(r)	
	#print(s)
	#print(r[0].values())
	context = {
		'f': f,
		#'values': values
	}	
	#return HttpResponse(z+" "+itemName+" "+quantity+" "+totalprice)
	return render(request, "webportal/cart.html", context)