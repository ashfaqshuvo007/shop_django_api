"""
    Created by tareq on ২০/৯/১৯
"""
from rest_framework.serializers import ModelSerializer

from sol_factory.base.serializers.domain_entity_serializer import DomainEntitySerializer
from sol_factory.users.models import ContactInformation

__author__ = "Tareq"


class ContactInformationSerializer(DomainEntitySerializer):
    class Meta:
        model = ContactInformation
        fields = [
            'id', 'tsync_id', 'email_address', 'alternative_email_address', 'contact_number', 'street_address'
        ]
