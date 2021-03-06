"""
    Created by tareq on ২/৭/১৯
"""
from sol_factory.users.enums.user_type_enum import UserTypeEnum
from sol_factory.users.enums.verification_status_enum import VerificationStatusEnum
from sol_factory.users.managers.model_managers.staff_manager import SolFactoryStaffUserManager
from sol_factory.users.models import ConsoleUser

__author__ = "Tareq"


class SolFactoryStaffUser(ConsoleUser):
    objects = SolFactoryStaffUserManager()

    class Meta:
        app_label = 'users'
        proxy = True

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.verification_status = VerificationStatusEnum.Verified.value
        self.is_staff = True
        self.user_type = UserTypeEnum.Staff.value
        super(SolFactoryStaffUser, self).save(
            force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields)
