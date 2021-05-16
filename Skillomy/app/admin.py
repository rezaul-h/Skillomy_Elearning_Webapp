from django.contrib import admin
from .models import(
	Customer,
	Product,
	Categories,
	Cart,
	OrderPlaced,
	Teacher,
	Content
	)  
# Register your models here.
#@admin.register(Customer)
#class CustomerModelAdmin(admin.ModelAdmin):
#	list_display=['id','user','name','biography','language','city','website','zipcode','state']

#@admin.register(Teacher)
#class TeacherModelAdmin(admin.ModelAdmin):
#	list_display=['id','user','name','university_name','category','experience','time_invest',
#	'biography','language','city','website']

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
	list_display=['id','title','selling_price','discounted_price','description','level','category_id','content','product_image']

@admin.register(Categories)
class CateogriesModelAdmin(admin.ModelAdmin):
	list_display=['id','name']

@admin.register(Content)
class ContentModelAdmin(admin.ModelAdmin):
	list_display=['id','category_name','slides','lectures']

#@admin.register(Cart)
#class CartModelAdmin(admin.ModelAdmin):
#	list_display=['id','user','course','quantity']

#@admin.register(OrderPlaced)
#class OrderPlacedModelAdmin(admin.ModelAdmin):
#	list_display=['id','user','customer','course','quantity','ordered_date','status']

