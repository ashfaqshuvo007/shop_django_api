"""
    Created by tareq on ২৩/৬/১৯
"""
from django.core.management import BaseCommand

from sol_factory.users.enums.user_type_enum import UserTypeEnum
from sol_factory.users.enums.verification_status_enum import VerificationStatusEnum
from sol_factory.users.models import ConsoleUser

__author__ = "Tareq"


class Command(BaseCommand):
    def handle(self, *args, **options):
        admin_user = ConsoleUser.objects.filter(username='sfadmin').first()
        if not admin_user:
            print("Creating admin user...")
            admin_user = ConsoleUser(
                username='sfadmin', first_name='System', last_name='Admin',
                verification_status=VerificationStatusEnum.Verified.value,
                user_type=UserTypeEnum.Admin.value, is_staff=True, is_superuser=True
            )
            admin_user.set_password('SFadmin123#')
            admin_user.save()
            print("...Created")
        else:
            print("Admin user already exists. Skipping...")
