"""
    Created by tareq on ১১/৬/১৯
"""
from django.contrib.auth.models import AbstractUser
from django.db.models import SmallIntegerField, ImageField, OneToOneField, \
    PROTECT

from sol_factory.base.models.domain_entity import DomainEntity
from sol_factory.users.enums.user_type_enum import UserTypeEnum
from sol_factory.users.enums.verification_status_enum import VerificationStatusEnum

__author__ = "Tareq"


class ConsoleUser(DomainEntity, AbstractUser):
    verification_status = SmallIntegerField(
        default=VerificationStatusEnum.Unverified.value, choices=VerificationStatusEnum.get_choices())
    profile_info = OneToOneField('users.UserProfileInfo', null=True, on_delete=PROTECT)
    user_type = SmallIntegerField(null=True, choices=UserTypeEnum.get_choices())
    photo = ImageField(blank=True, null=True)

    class Meta:
        app_label = 'users'

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self.first_name:
            if self.last_name:
                self.name = "{} {}".format(self.first_name, self.last_name)
            else:
                self.name = self.first_name
        else:
            if self.last_name:
                self.name = self.last_name
            else:
                self.name = self.username
        super(ConsoleUser, self).save(force_insert=force_insert, force_update=force_update, using=using,
                                      update_fields=update_fields)
