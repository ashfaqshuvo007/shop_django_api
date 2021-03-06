"""
    Created by tareq on ২০/৯/১৯
"""

from sol_factory.base.serializers.domain_entity_serializer import DomainEntitySerializer
from sol_factory.users.models import SourcingInformation

__author__ = "Tareq"


class SourcingInformationSerializer(DomainEntitySerializer):
    class Meta:
        model = SourcingInformation
        fields = [
            'id', 'tsync_id', 'annual_purchase_volume', 'preferred_supplier_qualification',
            'primary_sourcing_purpose', 'preferred_industries', 'average_sourcing_frequency',
        ]
