"""
    Created by tareq on ১৯/৯/১৯
"""
from django.db.models import OneToOneField, PROTECT

from sol_factory.base.models import DomainEntity

__author__ = "Tareq"


class UserProfileInfo(DomainEntity):
    basic_profile_info = OneToOneField('users.BasicProfileInfo', null=True, on_delete=PROTECT)
    contact_address = OneToOneField('users.ContactInformation', null=True, on_delete=PROTECT)
    company_information = OneToOneField('users.Company', null=True, on_delete=PROTECT)
    sourcing_information = OneToOneField('users.SourcingInformation', null=True, on_delete=PROTECT)

    class Meta:
        app_label = 'users'
