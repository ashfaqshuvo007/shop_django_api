"""
    Created by tareq on ২৮/৬/১৯
"""

from sol_factory.base.serializers.domain_entity_serializer import DomainEntitySerializer
from sol_factory.products.models import ProductCategory
from sol_factory.products.serializers.product_attribute_serializer import ProductAttributeSerializer
from sol_factory.products.serializers.product_icon_serializer import ProductIconSerializer

__author__ = "Tareq"


class ProductCategorySerializer(DomainEntitySerializer):
    icons = ProductIconSerializer(many=True, required=False)
    attributes = ProductAttributeSerializer(many=True, required=False)

    class Meta(DomainEntitySerializer.Meta):
        model = ProductCategory
        fields = DomainEntitySerializer.Meta.fields + [
            'id', 'name', 'tsync_id', 'parent', 'description', 'attributes', 'icons'
        ]
