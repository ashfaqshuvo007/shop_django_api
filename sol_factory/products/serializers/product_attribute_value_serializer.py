"""
    Created by tareq on ৪/৮/১৯
"""

from sol_factory.base.serializers.domain_entity_serializer import DomainEntitySerializer
from sol_factory.products.models import ProductAttributeValue
from sol_factory.products.serializers.product_attribute_serializer import ProductAttributeGETSerializer

__author__ = "Tareq"


class ProductAttributeValueGETSerializer(DomainEntitySerializer):
    product_attribute = ProductAttributeGETSerializer()

    class Meta(DomainEntitySerializer.Meta):
        model = ProductAttributeValue
        fields = [
            'product_attribute', 'note', 'value', 'id'
        ]


class ProductAttributeValueSerializer(DomainEntitySerializer):
    class Meta(DomainEntitySerializer.Meta):
        model = ProductAttributeValue
        fields = DomainEntitySerializer.Meta.fields + [
            'product_attribute', 'note', 'value', 'id'
        ]
