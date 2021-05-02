from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['user', 'product_name', 'selling_price', 'in_stock']
    list_filter = ['in_stock']
    search_fields = ['product_name',]


@admin.register(RatingReview)
class RatingReviewAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'rating', 'date']
    list_filter = ['rating']
    search_fields = ['product_name']