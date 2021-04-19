from django.contrib import admin
from .models import(
	Customer,
	Product,
	Cart,
	OrderPlaced
	)  
# Register your models here.
@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
	list_display=['id','user','name','biography','language','city','website','zipcode','state']

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
	list_display=['id','title','selling_price','discounted_price','description','category','product_image']

@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
	list_display=['id','user','course','quantity']

@admin.register(OrderPlaced)
class OrderPlacedModelAdmin(admin.ModelAdmin):
	list_display=['id','user','customer','course','quantity','ordered_date','status']

