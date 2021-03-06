from django.shortcuts import render

from django.http import HttpResponse

from .forms import *

from .models import *

# For sending Email
from django.core.mail import send_mail

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
	#elif(product_name=="paints"):
	#	form = paintsform(request.POST or None)
	#	p_name = "Paints and Hardware"
	else:
		return HttpResponse(" there is no such thing")

	context = {
		"form" : form,
		"p_name": p_name
	}
	return render(request, "webportal/productform.html", context)

def price(request, product_name):
	if(product_name == "cement"):
		# Putting the forms data into variables
		#result of queries
		resquery1 = request.POST.get('Company_Name')
		resquery2 = request.POST.get('Type')
		resquery3 = request.POST.get('Grade')

		# This needs to be passed as a context
		queries = {
			'Company Name': resquery1,
			'Type of Cement': resquery2,
			'Grade of Cement': resquery3,
		}

		# Query filteration
		x = Cement.objects.filter(Company_Name = resquery1, Type_of_Cement = resquery2, Grade_of_Cement = resquery3)

	elif(product_name == "course"):
		# Putting the course aggregate forms data into variables

		#result of queries
		resquery1 = request.POST.get('Place_of_Import')
		resquery2 = request.POST.get('Size_of_Course')
		resquery3 = request.POST.get('Quantity_of_Course')

		# This needs to be passed as a context
		queries = {
			'Place of Import': resquery1,
			'Size of course': resquery2,
			'Quantity of Course': resquery3,
		}

		# Query filteration
		x = CourseAggregate.objects.filter(Place_of_course = resquery1, Size_of_course = resquery2, Amount_of_course = resquery3)

	elif(product_name == "brick"):
		# Putting the Brick forms data into variables

		#result of queries
		resquery1 = request.POST.get('Companies_Available')
		resquery2 = request.POST.get('Brick_or_Tile')
		resquery3 = request.POST.get('Grade')

		# These needs to be passed as a context
		queries = {
			'Companies Available': resquery1,
			'Brick or Tile': resquery2,
			'Grade of Brick/Tile': resquery3,
		}

		# Query filteration
		x = BrickOrTile.objects.filter(Brand_of_Brick = resquery1, Brick_or_Tiles = resquery2, Grade_of_Brick = resquery3)

	elif(product_name == "tanker"):
		# Putting the course aggregate forms data into variables

		#result of queries
		resquery1 = request.POST.get('Company_of_tanker')
		resquery2 = request.POST.get('Capacity_of_tanker')

		# These needs to be passed as a context
		queries = {
			'Company Name': resquery1,
			'Capacity of Tanker': resquery2,
		}

		# Query filteration
		x = WaterTanker.objects.filter(Company_of_tanker = resquery1, Capacity_of_Tanker = resquery2)

	elif(product_name == "sand"):
		# Putting the course aggregate forms data into variables

		#result of queries
		resquery1 = request.POST.get('Type_of_sand')

		# These needs to be passed as a context
		queries = {
			'Type of Sand': resquery1,
		}

		# Query filteration
		x = Sand.objects.filter(Type_of_Sand = resquery1)

	else:
		return HttpResponse("No such Item present")

	resquery4 = request.POST.get('Total_Quantity')

	for tempobject in x:
		modelprice = tempobject.Price
		modelid = int(tempobject.ids)

	totalprice = str(modelprice*float(resquery4))

	context = {
		"totalprice": totalprice,
		"p_name": product_name,
		"modelid": modelid,
		'quantity': resquery4,
		'queries': queries,
	}

	request.session['totalprice'] = totalprice
	request.session['p_name'] = product_name
	request.session['modelid'] = modelid
	request.session['Amount'] = resquery4

	# At the end return the response
	return render(request, "webportal/price.html", context)

def cart(request):

	# Let's put the session variables into a variable.
	modelid = request.session.get('modelid')
	product_name = request.session.get('p_name')
	quantity = request.session.get('Amount')
	totalprice = request.session.get('totalprice')
	userName = request.user.username

	# It's time to add a field to the cart model
	if(modelid != None and userName != ""):
		addfield = Cart(product_id=modelid, product_name=product_name, Quantity=quantity, Amount=totalprice, userName = userName)
		addfield.save()
		# Now delete the session variables.
		del request.session['modelid']
		del request.session['p_name']
		del request.session['Amount']
		del request.session['totalprice']

	# All the products will stay in this dictionary
	allproducts = {}
	productList = []

	# Put all the data in Cart model into a variable
	cart = Cart.objects.filter(userName = userName)

	# Now loop through each item in the cart
	for cartitem in cart:

		p_name = cartitem.product_name
		p_id = cartitem.product_id
		p_totalprice = cartitem.Amount
		p_quantity = cartitem.Quantity

		if(p_name == "cement"):
			# Go on and search the item in the cement model
			searchtable = Cement.objects.filter(ids = p_id)

			for singlerow in searchtable:
				# Now create variables using seartable
				company_name = singlerow.Company_Name
				type_of_cement = singlerow.Type_of_Cement
				grade_of_cement = singlerow.Grade_of_Cement
				single_item_price = singlerow.Price

				# Now create a dictionary that can be passed to the HTML to show
				productData = {
					'Company Name': company_name,
					'Type of Cement': type_of_cement,
					'Grade of Cement': grade_of_cement,
					'Price of Single Item': single_item_price,
				}

		elif(p_name == "course"):

			# Do the same as done in the if statment
			searchtable = CourseAggregate.objects.filter(ids = p_id)

			for singlerow in searchtable:
				place_of_import = singlerow.Place_of_course
				size_of_course = singlerow.Size_of_course
				amount_of_course = singlerow.Amount_of_course
				single_item_price = singlerow.Price

				productData = {
					'Place of Import': place_of_import,
					'Size of course': size_of_course,
					'Quantity of Course': amount_of_course,
					'Price of Single Item': single_item_price,
				}

		elif(p_name == "brick"):

			searchtable = BrickOrTile.objects.filter(ids = p_id)

			for singlerow in searchtable:
				company_name = singlerow.Brand_of_Brick
				type_of_brick = singlerow.Brick_or_Tiles
				grade_of_brick = singlerow.Grade_of_Brick
				single_item_price = singlerow.Price

				productData = {
					'Company Name': company_name,
					'Type of Cement': type_of_brick,
					'Grade of Cement': grade_of_brick,
					'Price of Single Item': single_item_price,
				}

		elif(p_name == "tanker"):

			searchtable = WaterTanker.objects.filter(ids = p_id)

			for singlerow in searchtable:
				company_name = singlerow.Company_of_tanker
				type_of_brick = singlerow.Capacity_of_Tanker
				single_item_price = singlerow.Price

				productData = {
					'Company Name': company_name,
					'Type of Cement': type_of_brick,
					'Price of Single Item': single_item_price,
				}

		elif(p_name == "sand"):

			searchtable = Sand.objects.filter(ids = p_id)

			for singlerow in searchtable:
				type_of_sand = singlerow.Type_of_Sand
				single_item_price = singlerow.Price

				productData = {
					'Company Name': company_name,
					'Price of Single Item': single_item_price,
				}
		else:
			print("Nothing found")

		# Update products data dictionary
		productData.update({'Product': p_name})
		productData.update({'totalprice': p_totalprice})
		productData.update({'Amount': p_quantity})

		# Update all products dictionary
		allproducts.update({'Products': productData})

		for value in allproducts.items():
			productList.extend(value)

	form = checkoutcart(request.POST or None)

	request.session['sendcart'] = productList
	request.session['username'] = userName

	context = {
        'form' : form,
		'productList': productList,
	}


	return render(request, "webportal/cart.html", context)

# Now I will code for the social authentication features in the app.
def login(request):
    return render(request, "webportal/login.html")

# Here is the code to checkout from the cart. That is to send the mail of the
# cart.

def sendMail(request):

    Name = request.POST.get('Name')
    Email = request.POST.get('Email')
    Address = request.POST.get('Address')
    Phone_number = request.POST.get('Phone_number')
    custom_msg = request.POST.get('custom_msg')

    message = ''
    chrome = []

    sendcart = request.session.get('sendcart')
    
    c = 0
    a = 0
    for allproducts in sendcart:
    	c = c + 1
    	if(c%2 != 0):
    		continue
    	chrome.insert(a, allproducts)
    	a = a + 1
    	for somechrome in chrome:
    		for key, value in somechrome.items():
    			message = message + str(key) + '---------' + str(value) + '\n'
    		message = message + '\n'

    username = request.session.get('username')

    subject = 'Please deliver these things'
    #message = 'Trying to send khali msg ' + sendcart
    send_email_from = Email
    send_email_to = 'ranvir.singh1114@gmail.com'


    send_mail(subject, message, send_email_from, [send_email_to], fail_silently=False)
    html = message
    return HttpResponse(html)





