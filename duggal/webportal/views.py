from django.shortcuts import render

from django.http import HttpResponse

from .forms import *

from .models import *
# Create your views here.

# This is the simplest view for index.html page
def index(request):
    return render(request, 'webportal/index.html', {})

# This view is opened when the user want to buy a product from the list
def product(request, product_name):
	# If the user want to buy cement
	if(product_name=="cement"):
		form = cementform(request.POST or None)
		p_name = "Cement"

	# else if the user want to buy course aggregate
	elif(product_name=="course"):
		form = courseform(request.POST or None)
		p_name = "Course Aggregate"

	# else if the user want to buy sand
	elif(product_name=="sand"):
		form = sandform(request.POST or None)
		p_name = "Sand"

	# else if the user want to buy paints and hardware
	elif(product_name=="brick"):
		form = brickform(request.POST or None)
		p_name = "Bricks or Tiles"

	# else if the user want to buy Bricks and Tiles
	elif(product_name=="tanker"):
		form = tankerform(request.POST or None)
		p_name = "Water Tankers"

	# else if the user want to buy Water Tankers
	elif(product_name=="paints"):
		form = paintsform(request.POST or None)
		p_name = "Paints and Hardware"

	context = {
		"form" : form,
		"p_name": p_name
	}
	return render(request, "webportal/productform.html", context)

def output(request):
	query1 = request.POST.get('company_Name')
	query2 = request.POST.get('Type')
	query3 = request.POST.get('Grade')
	query4 = request.POST.get('Total_Quantity')
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
	
	# temp variable d will be used for the looping process
	d = 0
	# f will contain all the things in the cart.
	f = cart.objects.all()
	w = [] # list w will contain correspoding values from cement model. 
	for a in f:
		# b will store all the ids in the cart in iteration
		b = a.product_id
		w.insert(d, Cement.objects.filter(ids=b))
		d = d+1

	d = 0
	r = {}
	f = []
	for e in w:
		r = vars(e[0])
		print(r)		
		f.insert(d, r)
		d = d+1

	context = {
		'f': f,
	}	
	return render(request, "webportal/cart.html", context)

# views for course aggregate


def courseprice(request):
	query1 = request.POST.get('Place_of_Import')
	query2 = request.POST.get('Size_of_Course')
	query3 = request.POST.get('Quantity_of__Course')
	query4 = request.POST.get('Total_Quantity')
	x = CourseAggregate.objects.filter(Place_of_course = query1, Size_of_course = query2, Amount_of_course = query3)
	
	for m in x:
		z = m.Price_of_Course

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
	return render(request, "webportal/courseprice.html", context)

def inputcourse(request):
	# get all the session variables into some local variables
	quantity = request.session.get('quantity')
	totalprice = request.session.get('totalprice')
	ids = request.session.get('ids')

	# Put them into the cart model/database
	x = cart(product_id=ids, Quantity=quantity, Amount=totalprice)
	x.save()
	
	# temp variable d will be used for the looping process
	d = 0
	# f will contain all the things in the cart.
	f = cart.objects.all()
	w = [] # list w will contain correspoding values from cement model. 
	for a in f:
		# b will store all the ids in the cart in iteration
		b = a.product_id
		w.insert(d, CourseAggregate.objects.filter(ids=b))
		d = d+1

	d = 0
	r = {}
	f = []
	for e in w:
		r = vars(e[0])
		print(r)		
		f.insert(d, r)
		d = d+1

	context = {
		'f': f,
	}	
	return render(request, "webportal/cart.html", context)



#def bekaar(request, p_id):
	#return HttpResponse("That is very fine dick %s" %p_id)
