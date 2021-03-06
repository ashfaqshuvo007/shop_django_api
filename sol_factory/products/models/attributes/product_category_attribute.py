"""
    Created by tareq on 8/15/19
"""
from django.db.models import ForeignKey, PROTECT, TextField

from sol_factory.base.models import DomainEntity

__author__ = "Tareq"


class ProductCategoryAttribute(DomainEntity):
    product_category = ForeignKey('products.ProductCategory', on_delete=PROTECT, related_name='category_attributes')
    product_attribute = ForeignKey('products.ProductAttribute', on_delete=PROTECT, related_name='category_attributes')
    options = TextField(blank=True)

    class Meta:
        app_label = 'products'
