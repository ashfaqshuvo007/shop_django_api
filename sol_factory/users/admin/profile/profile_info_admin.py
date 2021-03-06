"""
    Created by tareq on ২০/৯/১৯
"""
from django.contrib import admin
from django.contrib.admin import ModelAdmin

from sol_factory.users.models import UserProfileInfo

__author__ = "Tareq"


@admin.register(UserProfileInfo)
class UserProfileInfoAdmin(ModelAdmin):
    fields = [
        'basic_profile_info', 'contact_address', 'company_information'
    ]
