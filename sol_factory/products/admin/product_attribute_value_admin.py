"""
    Created by shakib on 03/08/2019
"""
from django.contrib import admin
from django.contrib.admin import ModelAdmin

from sol_factory.products.models import ProductAttributeValue

__author__ = "Shakib"


@admin.register(ProductAttributeValue)
class ProductAttributeValueAdmin(ModelAdmin):
    list_display = (
        'category_attribute', 'name', 'note', 'value'
    )
    list_filter = ('category_attribute',)
    fields = ('category_attribute', 'name', 'note', 'value',)
