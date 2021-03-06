"""
    Created by tareq on 9/28/19
"""

from sol_factory.base.utils.extras.base_enum import BaseEnum

__author__ = "Tareq"


class OrderStatusEnum(BaseEnum):
    Pending = 0
    Confirmed = 10
    Delivered = 20
    Received = 30
