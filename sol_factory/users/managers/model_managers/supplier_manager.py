"""
    Created by tareq on ২/৭/১৯
"""
from django.contrib.auth.base_user import BaseUserManager

from sol_factory.users.enums.user_type_enum import UserTypeEnum

__author__ = "Tareq"


class SolFactorySupplierUserManager(BaseUserManager):
    def get_queryset(self):
        return super(SolFactorySupplierUserManager, self).get_queryset().filter(
            user_type__in=[UserTypeEnum.Supplier.value, UserTypeEnum.BuyerAndSupplier.value])
