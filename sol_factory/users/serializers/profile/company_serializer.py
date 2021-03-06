"""
    Created by tareq on ৩০/৬/১৯
"""
from rest_framework.serializers import ModelSerializer

from sol_factory.base.serializers.domain_entity_serializer import DomainEntitySerializer
from sol_factory.users.models import Company

__author__ = "Tareq"


class CompanySerializer(DomainEntitySerializer):
    class Meta:
        model = Company
        fields = [
            'id', 'tsync_id',  'name', 'registered_country', 'operational_country', 'city_name', 'zip_code', 'address',
            'number_of_employees', 'registration_year', 'company_website', 'annual_revenue', 'photo'
        ]
