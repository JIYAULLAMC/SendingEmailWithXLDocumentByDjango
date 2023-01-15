from django.contrib import admin

# Register your models here.

from .models import Customer, Product, OrderPlaced, Cart


@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ["user","name","lacality","city","zipcode","state",]


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ["title","selling_price","discounted_price","description","brand","category","product_image",]



@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ["user","product", "quantity"]


@admin.register(OrderPlaced)
class OrderPlacedModelAdmin(admin.ModelAdmin):
    list_display = ["user","customer","product","quantity","ordered_date","status",]


