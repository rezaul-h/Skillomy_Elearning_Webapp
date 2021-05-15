from django.shortcuts import render,redirect
from django.views import View
from django.views.generic import ListView,DetailView,CreateView
from .models import Customer, Product, Cart, OrderPlaced,Teacher,Categories
from .forms import CustomerRegistrationForm, CustomerProfileForm,TeacherRegistrationForm
from django.contrib import messages
from django.http import JsonResponse
#from example.config import pagination
from django.db.models import Q
import joblib

def Allcourse(request):
	results=Product.objects.all()
	return render(request,'app/allproducts.html',{'results':results})

class HomeView(ListView):
	model=Product
	template_name='app/create_course.html'

class AddCourseView(CreateView):
	model=Product
	template_name='app/course_add.html'
	fields=['id','title','selling_price','discounted_price','description','level','category']


class ProductView(View):
	def get(self,request):
		python=Product.objects.filter(category='Py')
		MachineLearning=Product.objects.filter(category='ML')
		DataScience=Product.objects.filter(category='DS')
		DeepLearning=Product.objects.filter(category='DL')
		context={
		'python':python,
		'MachineLearning':MachineLearning,
		'DataScience':DataScience,
		'DeepLearning':DeepLearning

		}
		return render(request,'app/home.html',context)


class ProductDetailView(View):
	def get(self,request,pk):
		course=Product.objects.get(pk=pk)
		context={'course':course}
		return render (request, 'app/productdetail.html',context)


class CustomerRegistrationView(View):
	def get(self, request):
		form=CustomerRegistrationForm()
		return render(request,'app/customerregistration.html',{'form':form})
	def post(self,request):
		form=CustomerRegistrationForm(request.POST)
		if form.is_valid():
			messages.success(request,'Congratulations ! Registration Sucessful')
			form.save()
		return render(request,'app/customerregistration.html',{'form':form})

class TeacherRegistrationView(View):
	def get(self, request):
		form=TeacherRegistrationForm()
		return render(request,'app/teacherregistration.html',{'form':form})
	def post(self,request):
		form=TeacherRegistrationForm(request.POST)
		if form.is_valid():
			messages.success(request,'Congratulations ! Registration Sucessful')
			form.save()
		return render(request,'app/teacherregistration.html',{'form':form})

class ProfileView(View):
	def get(self,request):
		form=CustomerProfileForm()
		return render(request,'app/profile.html',{'form':form, 'active':'btn-secondary'})
	def post(self,request):
		form=CustomerProfileForm(request.POST)
		reg=Customer.objects.get(user=request.user)
		if form.is_valid():
			usr=request.user
			name=form.cleaned_data['name']
			biography=form.cleaned_data['biography']
			language=form.cleaned_data['language']
			city=form.cleaned_data['city']
			website=form.cleaned_data['website']
			zipcode=form.cleaned_data['zipcode']
			state=form.cleaned_data['state']
			#reg=Customer(user=usr,name=name,biography=biography,language=language,city=city,website=website,zipcode=zipcode,state=state)
			reg.user=usr
			reg.name=name
			reg.biography=biography
			reg.language=language
			reg.city=city
			reg.website=website
			reg.zipcode=zipcode
			reg.state=state
			reg.save()
			#messages.success(request,'Congratulations ! Registration Sucessful')
			messages.success(request,'Profile updated')
		return render(request,'app/profile.html',{'form':form,'active':'btn-secondary'})



def add_to_cart(request):
	user=request.user
	course_id=request.GET.get('course_id',None)
	course=Product.objects.get(id=course_id)
	Cart(user=user,course=course).save()
	return redirect('/cart')

def show_cart(request):
	if request.user.is_authenticated:
		user=request.user
		cart=Cart.objects.filter(user=user)
		total_actual=0.0
		total_ammount=0.0
		discount=0.0
		total_discount=0.0
		cart_product=[p for p in Cart.objects.all() if p.user==user]
		if cart_product:
			for p in cart_product:
				actual=p.quantity*p.course.selling_price
				total_actual+=actual
				discount=(p.course.selling_price - p.course.discounted_price)
				total_discount+=discount
				tempammount=(p.quantity * p.course.discounted_price)
				total_ammount+=tempammount
			context={'carts':cart, 'total_ammount':total_ammount,'total_discount':total_discount,'total_actual':total_actual}
			return render(request, 'app/addtocart.html',context)
		else:
			return render(request, 'app/emptycart.html')


def remove_cart(request):
	if request.method=='GET':
		prod_id=request.GET['prod_id']
		c=Cart.objects.get(Q(course=prod_id)&Q(user=request.user))
		c.delete()
		total_actual=0.0
		total_ammount=0.0
		discount=0.0
		total_discount=0.0
		cart_product=[p for p in Cart.objects.all() if p.user==request.user]
		for p in cart_product:
			actual=p.quantity * p.course.selling_price
			total_actual+=actual
			discount=(p.course.selling_price - p.course.discounted_price)
			total_discount+=discount
			tempammount=(p.quantity * p.course.discounted_price)
			total_ammount+=tempammount
		data={'total_ammount':total_ammount,'total_discount':total_discount,'total_actual':total_actual}	
		return JsonResponse(data)

def Search(request):
	query=request.GET["query"]
	results=Product.objects.filter(Q(title__icontains=query)|Q(description__icontains=query))
	return render(request,'app/search.html',{'results':results})
	


def buy_now(request):
 return render(request, 'app/buynow.html')

def address(request):
 return render(request, 'app/address.html')

def orders(request):
	op=OrderPlaced.objects.filter(user=request.user)
	return render(request, 'app/orders.html',{'op':op})

class QCheckFormView(View):
	def get(self,request):
		category=Categories.objects.all()
		return render(request,'app/qcheckform.html',{'category':category})

def prediction(request):
	classification=joblib.load("trainning.sav")
	list=[]
	list.append(request.GET['q1'])
	##list.append(request.GET['q2'])
	list.append(request.GET['q3'])
	list.append(request.GET['q4'])
	list.append(request.GET['q5'])
	list.append(request.GET['level'])
	
	ans=classification.predict([list])
	return render(request,'app/prediction.html',{'ans':ans})


		
def mobile(request,data=None):
	if data==None:
		mobiles=Product.objects.filter(category='M')
	elif data=='Redmi' or data=='Samsung':
		mobiles=Product.objects.filter(category='M').filter(brand=data)

	return render(request,'app/mobile.html',{'mobiles':mobiles})


def checkout(request):
	user=request.user
	address=Customer.objects.filter(user=user)
	cart_item=Cart.objects.filter(user=user)
	ammount=0.0
	total_ammount=0.0
	cart_product=[p for p in Cart.objects.all() if p.user==request.user]
	if cart_product:
		for p in cart_product:
			tempammount=(p.quantity * p.course.discounted_price)
			total_ammount+=tempammount
	return render(request, 'app/checkout.html',{'address':address,'total_ammount':total_ammount,'cart_item':cart_item})


def payment_done(request):
	user=request.user
	custid=request.GET.get('custid')
	customer=Customer.objects.get(id=custid)
	cart=Cart.objects.filter(user=user)
	for c in cart:
		OrderPlaced(user=user,customer=customer,course=c.course,quantity=c.quantity).save()
		c.delete()
	return redirect("orders")




#def Create_course(request):
#	return render(request, 'app/create_course.html')