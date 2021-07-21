from MiniMart.models import Customer, Order, Product, Tags
from django.contrib import admin

# Register your models here.

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Tags)