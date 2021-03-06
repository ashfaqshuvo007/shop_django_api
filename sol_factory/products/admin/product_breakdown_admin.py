"""
    Created by tareq on ২০/৭/১৯
"""
from django.contrib import admin
from django.contrib.admin import ModelAdmin

from sol_factory.products.models.product_breakdown import ProductBreakdown

__author__ = "Tareq"


@admin.register(ProductBreakdown)
class ProductBreakdownAdmin(ModelAdmin):
    list_display = ('product', 'original_price', 'selling_price', 'discount_amount', 'stock_quantity')
    list_filter = ('product',)
    fields = ('product', 'selling_price', 'discount_amount', 'stock_quantity', 'attribute_values')
