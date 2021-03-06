"""
    Created by tareq on ২/৭/১৯
"""
from django.contrib import admin
from django.contrib.admin import ModelAdmin

from sol_factory.products.models import Product

__author__ = "Tareq"


@admin.register(Product)
class ProductAdmin(ModelAdmin):
    list_display = (
        'name', 'category', 'is_new',
    )
    list_filter = ('category',)
    fields = ('name', 'category', 'description', 'icons',)
