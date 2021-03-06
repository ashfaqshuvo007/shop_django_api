"""
    Created by tareq on ২/৭/১৯
"""
from django.contrib import admin
from django.contrib.admin import ModelAdmin

from sol_factory.products.models import ProductCategory, ProductCategoryAttribute

__author__ = "Tareq"


@admin.register(ProductCategoryAttribute)
class ProductCategoryAttributeAdmin(ModelAdmin):
    list_display = ('product_category', 'product_attribute', 'options')
    fields = ('product_category', 'product_attribute', 'options',)
