"""
    Created by tareq on ৫/৭/১৯
"""
from django.contrib import admin
from django.contrib.admin import ModelAdmin

from sol_factory.products.models import ProductIcon

__author__ = "Tareq"


@admin.register(ProductIcon)
class ProductIconAdmin(ModelAdmin):
    list_display = [
        'order', 'title'
    ]
    fields = [
        'order', 'file', 'title'
    ]
