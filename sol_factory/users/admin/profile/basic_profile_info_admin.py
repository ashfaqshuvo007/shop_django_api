"""
    Created by tareq on ২/৭/১৯
"""
from django.contrib import admin
from django.contrib.admin import ModelAdmin

from sol_factory.users.models import BasicProfileInfo

__author__ = "Tareq"


@admin.register(BasicProfileInfo)
class BasicProdileInfoAdmin(ModelAdmin):
    list_display = [
        'first_name', 'last_name', 'country', 'join_date'
    ]
    fields = [
        'first_name', 'last_name', 'country',
    ]
