from django.contrib import admin

from ecomapp.models import Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display=['name','price','cat','pdetail','is_active']
    list_filter=['cat','is_active']



admin.site.register(Product,ProductAdmin)