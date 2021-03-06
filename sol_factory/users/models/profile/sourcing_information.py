"""
    Created by tareq on ১৯/৯/১৯
"""
from django.db.models import CharField

from sol_factory.base.models import DomainEntity

__author__ = "Tareq"


class SourcingInformation(DomainEntity):
    annual_purchase_volume = CharField(max_length=256, blank=True, default='', null=True)
    preferred_supplier_qualification = CharField(max_length=256, blank=True, default='', null=True)
    primary_sourcing_purpose = CharField(max_length=256, blank=True, default='', null=True)
    preferred_industries = CharField(max_length=256, blank=True, default='', null=True)
    average_sourcing_frequency = CharField(max_length=256, blank=True, default='', null=True)

    class Meta:
        app_label = 'users'
