"""
    Created by tareq on ২/৭/১৯
"""
from django.contrib import admin
from django.contrib.admin import ModelAdmin

from sol_factory.users.models.roles.buyer_user import SolFactoryBuyerUser

__author__ = "Tareq"


@admin.register(SolFactoryBuyerUser)
class BuyerAdmin(ModelAdmin):
    list_display = [
        'name', 'email'
    ]
    fields = (
        ('username', 'password'), 'first_name', 'last_name', 'email', 'photo', 'user_type', 'verification_status',
        'profile_info'
    )
