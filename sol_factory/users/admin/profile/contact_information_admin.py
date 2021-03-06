"""
    Created by tareq on ২০/৯/১৯
"""
from django.contrib import admin
from django.contrib.admin import ModelAdmin

from sol_factory.users.models import ContactInformation

__author__ = "Tareq"


@admin.register(ContactInformation)
class ContactInformationAdmin(ModelAdmin):
    list_display = [
        'email_address', 'alternative_email_address', 'contact_number', 'street_address'
    ]
    fields = [
        'email_address', 'alternative_email_address', 'contact_number', 'street_address'
    ]
