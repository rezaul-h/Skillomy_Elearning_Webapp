from django.db import models
from django.urls import reverse
from django.db.models import CharField
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator
LANGUAGE_CHOICES=(
	('English','English'),
	('Bangla','Bangla')
	)
CATEGORY_CHOICES=(
	('Py', 'python'),
	('DS', 'Data Science'),
	('ML', 'Machine Learning'),
	('DL', 'Deep Learning'),
	)
EXPERIENCE_CHOICES=(
	('Proffesional ', 'Proffesional'),
	('Taught before casually', 'Taught before casually'),
	('Never Taught', 'Never Taught'),
	)

TIME_CHOICES=(
	('I am very busy at the time (0-2 hours)', 'I am very busy at the time (0-2 hours)'),
	('Work on free time (2-4 hours)', 'Work on free time (2-4 hours)'),
	('I have a lot of flexibility (5+ hours)', 'I have a lot of flexibility (5+ hours)'),
	('Not Decided', 'Not Decided'),
	)
LEVEL_CHOICES=(
	('Beginner', 'Beginner'),
	('Advanced', 'Advanced'),
	('Intermediate', 'Intermediate'),
	('Expert', 'Expert'),
	)

STATE_CHOICES=(
	('Ghorashal','Ghorashal'),
	('Monohardi','Monohardi'),
	('Shibpur','Shibpur'),
	('Raipura','Raipura'),
	('Madhabdi','Madhabdi'),
	('Mirzapur','Mirzapur'),
	('Dhanbari','Dhanbari'),
	('Madhupur','Madhupur'),
	('Chhagalnaiya','Chhagalnaiya'),
	('Parshuram','Parshuram'),
	('Bandarban','Bandarban'),
	('Rangamati','Rangamati')
	)
DEFAULT_USER_ID=1

class Customer(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	name=models.CharField(max_length=50, default="root")
	biography=CharField(max_length=100,default="N/A")
	language=CharField(choices=LANGUAGE_CHOICES,max_length=7,default="English")
	city=models.CharField(max_length=20,default="Dhaka")
	website=models.CharField(max_length=20,default="N/A")
	zipcode=models.IntegerField(default="zipcode")
	state=models.CharField(choices=STATE_CHOICES,max_length=50,default="Dhaka")


	def __str__(self):
		return str(self.id)


def get_default_customer():
	return Customer.objects.get(id=user)

class Teacher(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	customer=models.ForeignKey(Customer,on_delete=models.CASCADE,default=1)
	name=models.CharField(max_length=50)
	university_name=models.CharField(max_length=50)
	category=models.CharField(choices=CATEGORY_CHOICES, max_length=2)
	experience=models.CharField(choices=EXPERIENCE_CHOICES,max_length=30)
	time_invest=models.CharField(choices=TIME_CHOICES,max_length=100)
	biography=CharField(max_length=100,default="N/A")
	language=CharField(choices=LANGUAGE_CHOICES,max_length=7,default="English")
	city=models.CharField(max_length=20,default="Dhaka")
	website=models.CharField(max_length=20,default="N/A")
	


class Product(models.Model):
	title=models.CharField(max_length=50)
	selling_price= models.FloatField()
	discounted_price=models.FloatField()
	description=models.CharField(max_length=200)
	level=models.CharField(choices=LEVEL_CHOICES, max_length=20, default="Not sure")
	#brand=models.CharField(max_length=50)
	category=models.CharField(choices=CATEGORY_CHOICES, max_length=2,default=None)
	product_image=models.ImageField(upload_to='productimg',blank=True, null=True)

	def __str__(self):
		return str(self.id)

	def get_absolute_url(self):
		return reverse('create-course')

class Cart(models.Model):
	user=models.ForeignKey(User, on_delete=models.CASCADE)
	course=models.ForeignKey(Product,on_delete=models.CASCADE)
	quantity=models.PositiveIntegerField(default=1)

	def __str__(self):
		return str(self.id)
	
	@property
	def total_cost(self):
		return self.course.discounted_price
	

STATUS_CHOICES=(
	('Accepted','Accepted'),
	('Rejected','Rejected'),
	)

class OrderPlaced(models.Model):
	user=models.ForeignKey(User, on_delete=models.CASCADE)
	customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
	course=models.ForeignKey(Product,on_delete=models.CASCADE)
	quantity=models.PositiveIntegerField(default=1)
	ordered_date=models.DateTimeField(auto_now_add=True)
	status=models.CharField(max_length=30,choices=STATUS_CHOICES,default='Pending')





