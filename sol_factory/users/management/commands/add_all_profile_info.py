"""
    Created by tareq on ২৩/৬/১৯
"""
from django.core.management import BaseCommand

from sol_factory.users.models import ConsoleUser, UserProfileInfo, BasicProfileInfo, ContactInformation, Company, \
    SourcingInformation

__author__ = "Tareq"


class Command(BaseCommand):
    def handle(self, *args, **options):
        users = ConsoleUser.objects.filter(profile_info__isnull=True)
        for user in users:
            profile_info = UserProfileInfo()
            basic_profile_info = BasicProfileInfo(
                first_name='',
                last_name=''
            )
            basic_profile_info.save()
            contact_info = ContactInformation(
                email_address=user.email, contact_number='',
                street_address=''
            )
            contact_info.save()
            company_info = Company(name='')
            company_info.save()
            sourcing_info = SourcingInformation()
            sourcing_info.save()

            profile_info.basic_profile_info = basic_profile_info
            profile_info.contact_address = contact_info
            profile_info.company_information = company_info
            profile_info.sourcing_information = sourcing_info
            profile_info.save()

            user.profile_info = profile_info
            user.save()
