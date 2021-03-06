"""
    Created by tareq on 8/16/19
"""
from django.db.models import ForeignKey, CASCADE

from sol_factory.products.models import AbstractAttributeValue

__author__ = "Tareq"


class RFQAttributeValue(AbstractAttributeValue):
    rfq = ForeignKey('rfq.RequestForQuotation', related_name='rfq_attributes', on_delete=CASCADE)

    class Meta:
        app_label = 'rfq'
