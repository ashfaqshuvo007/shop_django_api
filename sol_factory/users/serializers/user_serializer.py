"""
    Created by tareq on ১৪/৬/১৯
"""
from django.db import transaction
from rest_framework.serializers import ModelSerializer

from sol_factory.users.enums.verification_status_enum import VerificationStatusEnum
from sol_factory.users.models import ConsoleUser, UserVerificationLink, UserProfileInfo, BasicProfileInfo, \
    ContactInformation, Company, SourcingInformation

__author__ = "Tareq"


class ConsoleUserGETSerializer(ModelSerializer):
    class Meta:
        model = ConsoleUser
        fields = [
            'id', 'tsync_id', 'first_name',
        ]


class ConsoleUserSerializer(ModelSerializer):
    def create(self, validated_data):
        with transaction.atomic():
            _password = self.initial_data['password']
            self.instance = super(ConsoleUserSerializer, self).create(validated_data=validated_data)

            try:
                verification_link = UserVerificationLink.prepare_verification_link_for_user(user=self.instance)
                UserVerificationLink.send_verification_link_to_user(user=self.instance,
                                                                    verification_link=verification_link)

                self.instance.verification_status = VerificationStatusEnum.VerificationSent.value
            except:
                self.instance.verification_status = VerificationStatusEnum.Unverified.value

            self.instance.set_password(_password)
            self.instance.save()

            profile_info = UserProfileInfo()
            basic_profile_info = BasicProfileInfo(
                first_name=self.validated_data['first_name'],
                last_name=self.validated_data['last_name'])
            basic_profile_info.save()
            contact_info = ContactInformation(
                email_address=self.validated_data['email'], contact_number=self.initial_data.get('contact_number', ''),
                street_address=self.initial_data.get('address', '')
            )
            contact_info.save()
            company_info = Company(name=self.initial_data.get('company_name', ''))
            company_info.save()
            sourcing_info = SourcingInformation()
            sourcing_info.save()

            profile_info.basic_profile_info = basic_profile_info
            profile_info.contact_address = contact_info
            profile_info.company_information = company_info
            profile_info.sourcing_information = sourcing_info
            profile_info.save()

            self.instance.profile_info = profile_info
            self.instance.save()

            return self.instance

    class Meta:
        model = ConsoleUser
        fields = [
            'id', 'tsync_id', 'username', 'first_name', 'last_name', 'email', 'user_type', 'verification_status',
        ]
        read_only_fields = ['verification_status']
