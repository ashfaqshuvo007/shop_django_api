"""
    Created by tareq on ২/৭/১৯
"""
from django.contrib import admin
from django.contrib.admin import ModelAdmin

from sol_factory.users.models.roles.staff_user import SolFactoryStaffUser

__author__ = "Tareq"


@admin.register(SolFactoryStaffUser)
class StaffAdmin(ModelAdmin):
    list_display = [
        'name', 'email',
    ]
    fields = (
        ('username', 'password'), 'first_name', 'last_name', 'email', 'photo'
    )
