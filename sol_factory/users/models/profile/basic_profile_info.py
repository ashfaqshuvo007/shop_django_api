"""
    Created by tareq on ১৯/৯/১৯
"""
from django.db.models import CharField, DateField, ForeignKey, SET_NULL

from sol_factory.base.models import DomainEntity, Country

__author__ = "Tareq"


class BasicProfileInfo(DomainEntity):
    first_name = CharField(blank=True, default='', null=True, max_length=127)
    last_name = CharField(blank=True, default='', null=True, max_length=127)
    country = ForeignKey(Country, null=True, on_delete=SET_NULL, related_name='registered_users')
    join_date = DateField(auto_now_add=True, null=True)

    class Meta:
        app_label = 'users'
