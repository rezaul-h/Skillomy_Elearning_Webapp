from django.shortcuts import render
from django.views import View
from .models import Customer, Product, Cart, OrderPlaced
from .forms import CustomerRegistrationForm, CustomerProfileForm
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
 return render(request, 'app/addtocart.html')

def buy_now(request):
 return render(request, 'app/buynow.html')

def address(request):
 return render(request, 'app/address.html')

def orders(request):
 return render(request, 'app/orders.html')

def mobile(request,data=None):
	if data==None:
		mobiles=Product.objects.filter(category='M')
	elif data=='Redmi' or data=='Samsung':
		mobiles=Product.objects.filter(category='M').filter(brand=data)
		
	return render(request,'app/mobile.html',{'mobiles':mobiles})


def checkout(request):
 return render(request, 'app/checkout.html')
