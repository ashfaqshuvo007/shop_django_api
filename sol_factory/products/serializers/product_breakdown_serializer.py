"""
    Created by tareq on ২৯/৫/১৯
"""

from sol_factory.base.serializers.domain_entity_serializer import DomainEntitySerializer
from sol_factory.products.models.product_breakdown import ProductBreakdown
from sol_factory.products.serializers.product_attribute_value_serializer import ProductAttributeValueSerializer, \
    ProductAttributeValueGETSerializer
from sol_factory.products.serializers.product_get_serializer import ProductGETSerializer

__author__ = "Tareq"


class ProductBreakdownGETSerializer(DomainEntitySerializer):
    product = ProductGETSerializer()
    product_attributes = ProductAttributeValueGETSerializer(many=True, required=False)

    class Meta(DomainEntitySerializer.Meta):
        model = ProductBreakdown
        fields = [
            'product', 'product_attributes', 'original_price', 'discount_percent',
            'selling_price', 'discount_amount', 'stock_quantity', 'id',
        ]


class ProductBreakdownSerializer(DomainEntitySerializer):
    product_attributes = ProductAttributeValueSerializer(many=True, required=False)

    class Meta(DomainEntitySerializer.Meta):
        model = ProductBreakdown
        fields = DomainEntitySerializer.Meta.fields + [
            'product_attributes', 'original_price', 'discount_percent',
            'selling_price', 'discount_amount', 'stock_quantity', 'id',
        ]
