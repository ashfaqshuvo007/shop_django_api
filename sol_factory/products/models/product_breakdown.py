"""
    Created by tareq on ১৯/৭/১৯
"""
from math import ceil

from django.db.models import ForeignKey, CASCADE, IntegerField, FloatField

from sol_factory.base.models import DomainEntity

__author__ = "Tareq"


class ProductBreakdown(DomainEntity):
    product = ForeignKey('products.Product', null=True, on_delete=CASCADE, related_name='product_breakdowns')
    selling_price = FloatField(default=0)
    discount_amount = FloatField(default=0)
    stock_quantity = IntegerField(default=0)

    class Meta:
        app_label = 'products'

    @property
    def original_price(self):
        return self.selling_price + self.discount_amount

    @classmethod
    def get_dependent_field_list(cls):
        return ['product_attributes']

    @property
    def discount_percent(self):
        try:
            return ceil(100.0 * float(self.discount_amount / (self.original_price)))
        except:
            return 0
