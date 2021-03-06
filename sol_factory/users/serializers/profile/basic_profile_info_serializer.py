"""
    Created by tareq on ২০/৯/১৯
"""

from sol_factory.base.serializers.domain_entity_serializer import DomainEntitySerializer
from sol_factory.users.models import BasicProfileInfo

__author__ = "Tareq"


class BasicProfileInfoSerializer(DomainEntitySerializer):
    class Meta:
        model = BasicProfileInfo
        fields = [
            'id', 'tsync_id', 'first_name', 'last_name', 'country', 'join_date'
        ]
