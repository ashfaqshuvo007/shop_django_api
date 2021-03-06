"""
    Created by tareq on ২/৭/১৯
"""
from django.contrib.auth.base_user import BaseUserManager

from sol_factory.users.enums.user_type_enum import UserTypeEnum

__author__ = "Tareq"


class SolFactoryBuyerUserManager(BaseUserManager):
    def get_queryset(self):
        return super(SolFactoryBuyerUserManager, self).get_queryset().filter(
            user_type__in=[UserTypeEnum.Buyer.value, UserTypeEnum.BuyerAndSupplier.value])
