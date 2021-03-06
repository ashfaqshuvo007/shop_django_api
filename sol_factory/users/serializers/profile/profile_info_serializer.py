"""
    Created by tareq on ২০/৯/১৯
"""
from rest_framework.serializers import ModelSerializer

from sol_factory.base.serializers.domain_entity_serializer import DomainEntitySerializer
from sol_factory.users.models import UserProfileInfo
from sol_factory.users.serializers.profile.basic_profile_info_serializer import BasicProfileInfoSerializer
from sol_factory.users.serializers.profile.company_serializer import CompanySerializer
from sol_factory.users.serializers.profile.contact_information_serializer import ContactInformationSerializer
from sol_factory.users.serializers.profile.sourcing_information_serializer import SourcingInformationSerializer

__author__ = "Tareq"


class ProfileInfoSerializer(DomainEntitySerializer):
    basic_profile_info = BasicProfileInfoSerializer(required=False)
    contact_address = ContactInformationSerializer(required=False)
    company_information = CompanySerializer(required=False)
    sourcing_information = SourcingInformationSerializer(required=False)

    def update(self, instance, validated_data):
        return super(ProfileInfoSerializer, self).update(instance, validated_data)

    class Meta:
        model = UserProfileInfo
        fields = [
            'id', 'tsync_id', 'basic_profile_info', 'contact_address',
            'company_information', 'sourcing_information'
        ]
