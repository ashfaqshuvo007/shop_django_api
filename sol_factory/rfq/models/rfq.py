"""
    Created by tareq on 8/16/19
"""
from django.db.models import CharField, ForeignKey, PROTECT, TextField, ManyToManyField

from sol_factory.base.models import DomainEntity
from sol_factory.products.models import Product

__author__ = "Tareq"


class RequestForQuotation(DomainEntity):
    title = CharField(max_length=511)
    product_category = ForeignKey(
        'products.ProductCategory', null=True, blank=True, on_delete=PROTECT, related_name='rfqs')
    product_description = TextField()
    attachments = ManyToManyField('base.FileObject', related_name='rfqs')

    class Meta:
        app_label = 'rfq'

    def get_product_queryset_matching_rfq(self):
        queryset = Product.objects.filter(category=self.product_category)

        return queryset