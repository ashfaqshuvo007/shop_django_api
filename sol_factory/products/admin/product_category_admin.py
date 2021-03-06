"""
    Created by tareq on ২/৭/১৯
"""
from django.contrib import admin
from django.contrib.admin import ModelAdmin

from sol_factory.products.models import ProductCategory

__author__ = "Tareq"


@admin.register(ProductCategory)
class ProductCategoryAdmin(ModelAdmin):
    list_display = ('name', 'parent_category', 'number_of_products')
    fields = ('name', 'parent', 'description', 'icons')
