"""
    Created by shakib on 03/08/2019
"""
from django.contrib import admin
from django.contrib.admin import ModelAdmin

from sol_factory.products.models import ProductAttribute

__author__ = "Shakib"


@admin.register(ProductAttribute)
class ProductAttributeAdmin(ModelAdmin):
    list_display = (
        'name', 'purpose', 'behavior'
    )
    list_filter = ('behavior',)
    fields = ('name', 'purpose', 'behavior',)
