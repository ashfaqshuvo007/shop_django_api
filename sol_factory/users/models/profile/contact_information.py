"""
    Created by tareq on ১৯/৯/১৯
"""
from django.db.models import EmailField, CharField, TextField

from sol_factory.base.models import DomainEntity

__author__ = "Tareq"


class ContactInformation(DomainEntity):
    email_address = EmailField(max_length=127, blank=True, default='', null=True)
    alternative_email_address = EmailField(max_length=127, blank=True, default='', null=True)
    contact_number = CharField(max_length=127, blank=True, default='', null=True)
    street_address = TextField(blank=True)

    class Meta:
        app_label = 'users'
