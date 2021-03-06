"""
    Created by tareq on 10/4/19
"""
from django.contrib.postgres.fields import JSONField
from django.db.models import ForeignKey, CASCADE

from sol_factory.base.models import DomainEntity

__author__ = "Tareq"


class OrderVersion(DomainEntity):
    reference_order = ForeignKey('orders.Order', on_delete=CASCADE)
    json_body = JSONField(blank=True)

    class Meta:
        app_label = 'orders'
