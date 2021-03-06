"""
    Created by tareq on ২৯/৫/১৯
"""

from sol_factory.base.serializers.domain_entity_serializer import DomainEntitySerializer
from sol_factory.products.models import Product
from sol_factory.products.serializers import ProductIconSerializer
from sol_factory.products.serializers.product_breakdown_serializer import ProductBreakdownSerializer

__author__ = "Shakib"


class ProductSerializer(DomainEntitySerializer):
    icons = ProductIconSerializer(many=True, required=False)
    product_breakdowns = ProductBreakdownSerializer(many=True, required=False)

    def is_valid(self, raise_exception=False):
        valid = super(ProductSerializer, self).is_valid(raise_exception)
        return valid

    def validate(self, attrs):
        attrs = super(ProductSerializer, self).validate(attrs)
        return attrs

    def to_representation(self, instance):
        data = super(ProductSerializer, self).to_representation(instance)
        return data

    def to_internal_value(self, data):
        data = super(ProductSerializer, self).to_internal_value(data)
        return data

    def create(self, validated_data):
        instance = super(ProductSerializer, self).create(validated_data)
        return instance

    def update(self, instance, validated_data):
        instance = super(ProductSerializer, self).update(instance, validated_data)
        return instance

    class Meta(DomainEntitySerializer.Meta):
        model = Product
        fields = DomainEntitySerializer.Meta.fields + [
            'category', 'name', 'supplier', 'description', 'keyword',
            'icons', 'product_breakdowns', 'is_new'
        ]
