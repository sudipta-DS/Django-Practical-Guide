from django.contrib import admin
from .models import Address,Cart,CartItem,Collection,Customer,Order,orderItem,Products,Promotion
# Register your models here.

admin.site.register(Address)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Collection)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(orderItem)
admin.site.register(Products)
admin.site.register(Promotion)
