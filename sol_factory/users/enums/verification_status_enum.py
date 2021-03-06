"""
    Created by tareq on ২৩/৬/১৯
"""
from enum import Enum

__author__ = "Tareq"


class VerificationStatusEnum(Enum):
    Unverified = 0
    VerificationSent = 1
    Verified = 2

    @classmethod
    def get_choices(cls):
        return tuple(
            [(x.value, x.name) for x in cls]
        )
