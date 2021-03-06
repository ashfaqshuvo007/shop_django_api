"""
    Created by tareq on ২/৭/১৯
"""
from sol_factory.users.managers.model_managers.buyer_manager import SolFactoryBuyerUserManager
from sol_factory.users.models import ConsoleUser

__author__ = "Tareq"


class SolFactoryBuyerUser(ConsoleUser):
    objects = SolFactoryBuyerUserManager()

    class Meta:
        app_label = 'users'
        proxy = True
