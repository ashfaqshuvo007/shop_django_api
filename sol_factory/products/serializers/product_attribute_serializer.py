"""
    Created by tareq on ৪/৮/১৯
"""

from sol_factory.base.serializers.domain_entity_serializer import DomainEntitySerializer
from sol_factory.products.models import ProductAttribute

__author__ = "Tareq"


class ProductAttributeGETSerializer(DomainEntitySerializer):
    class Meta(DomainEntitySerializer.Meta):
        model = ProductAttribute
        fields = [
            'name', 'purpose', 'behavior', 'condition', 'id'
        ]


class ProductAttributeSerializer(DomainEntitySerializer):
    class Meta(DomainEntitySerializer.Meta):
        model = ProductAttribute
        fields = DomainEntitySerializer.Meta.fields + [
            'name', 'purpose', 'behavior', 'condition', 'id'
        ]
