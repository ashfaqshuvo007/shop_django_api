"""
    Created by tareq on ২/৭/১৯
"""
from django.contrib import admin
from django.contrib.admin import ModelAdmin

from sol_factory.users.models.roles.supplier_user import SolFactorySupplierUser

__author__ = "Tareq"


@admin.register(SolFactorySupplierUser)
class SupplierAdmin(ModelAdmin):
    list_display = [
        'name', 'email',
    ]
    fields = (
        ('username', 'password'), 'first_name', 'last_name', 'email', 'photo', 'user_type', 'verification_status',
        'profile_info'
    )
