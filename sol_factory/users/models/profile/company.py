"""
    Created by tareq on ২৯/৬/১৯
"""
from datetime import datetime

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import ForeignKey, SET_NULL, CharField, TextField, IntegerField, ImageField

from sol_factory.base.models import Country
from sol_factory.base.models.domain_entity import DomainEntity
from sol_factory.users.utils.options.annual_revenue import get_annual_revenue_options
from sol_factory.users.utils.options.number_of_employees import get_number_of_employees_options

__author__ = "Tareq"


class Company(DomainEntity):
    registered_country = ForeignKey(Country, null=True, on_delete=SET_NULL, related_name='registered_companies')
    operational_country = ForeignKey(Country, null=True, on_delete=SET_NULL, related_name='operational_companies')

    city_name = CharField(max_length=120, blank=True, default='', null=True)
    zip_code = CharField(max_length=30, blank=True, default='', null=True)
    address = TextField(blank=True, default='', null=True)

    number_of_employees = CharField(max_length=40, choices=get_number_of_employees_options(), blank=True)
    registration_year = IntegerField(
        null=True, validators=[MinValueValidator(limit_value=1850), MaxValueValidator(limit_value=datetime.now().year)])
    company_website = CharField(blank=True, max_length=140)

    annual_revenue = CharField(blank=True, max_length=50, choices=get_annual_revenue_options())
    photo = ImageField(null=True, blank=True)

    class Meta:
        app_label = 'users'
