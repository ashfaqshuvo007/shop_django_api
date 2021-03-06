"""
    Created by tareq on ২/৭/১৯
"""
from sol_factory.users.managers.model_managers.supplier_manager import SolFactorySupplierUserManager
from sol_factory.users.models import ConsoleUser

__author__ = "Tareq"


class SolFactorySupplierUser(ConsoleUser):
    objects = SolFactorySupplierUserManager()

    class Meta:
        app_label = 'users'
        proxy = True
