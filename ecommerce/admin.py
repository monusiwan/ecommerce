from django.contrib import admin
from .models.product import *
from .models.category import *
from .models.orders import *
# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=['name','price','description','image','category']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=['name']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display=['product','customer','quantity','price','date']
    
