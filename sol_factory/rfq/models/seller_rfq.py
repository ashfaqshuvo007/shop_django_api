"""
    Created by tareq on 8/17/19
"""
from django.db.models import ForeignKey, PROTECT

from sol_factory.base.models import DomainEntity

__author__ = "Tareq"


class SellerRFQ(DomainEntity):
    rfq = ForeignKey('rfq.RequestForQuotation', on_delete=PROTECT, related_name='seller_rfqs')
    seller = ForeignKey('users.ConsoleUser', on_delete=PROTECT, related_name='seller_rfqs')

    class Meta:
        app_label = 'rfq'
