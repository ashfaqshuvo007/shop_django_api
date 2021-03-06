"""
    Created by Shakib
"""
from sol_factory.base.models import Country
from sol_factory.base.serializers.domain_entity_serializer import DomainEntitySerializer

__author__ = "Shakib"


class CountrySerializer(DomainEntitySerializer):
    class Meta(DomainEntitySerializer.Meta):
        model = Country
        fields = DomainEntitySerializer.Meta.fields
