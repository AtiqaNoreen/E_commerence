from django.contrib import admin
# Register your models here.
from .models import Products, Cart, CartItem

admin.site.register(Products)
admin.site.register(Cart)
admin.site.register(CartItem)