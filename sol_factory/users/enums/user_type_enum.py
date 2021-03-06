"""
    Created by tareq on ১১/৬/১৯
"""
from enum import Enum

__author__ = "Tareq"


class UserTypeEnum(Enum):
    Admin = 0
    Staff = 1
    Buyer = 2
    Supplier = 3
    BuyerAndSupplier = 4

    @classmethod
    def get_choices(cls):
        return tuple(
            [(x.value, x.name) for x in cls]
        )