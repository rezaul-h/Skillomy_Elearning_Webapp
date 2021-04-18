from django.shortcuts import render
from django.views import View
from .models import Customer, Product, Cart, OrderPlaced
from .forms import CustomerRegistrationForm
from django.contrib import messages

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



def add_to_cart(request):
 return render(request, 'app/addtocart.html')

def buy_now(request):
 return render(request, 'app/buynow.html')

def profile(request):
 return render(request, 'app/profile.html')

def address(request):
 return render(request, 'app/address.html')

def orders(request):
 return render(request, 'app/orders.html')

def change_password(request):
 return render(request, 'app/changepassword.html')

def mobile(request,data=None):
	if data==None:
		mobiles=Product.objects.filter(category='M')
	elif data=='Redmi' or data=='Samsung':
		mobiles=Product.objects.filter(category='M').filter(brand=data)
		
	return render(request,'app/mobile.html',{'mobiles':mobiles})


def checkout(request):
 return render(request, 'app/checkout.html')
