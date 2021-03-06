"""
    Created by tareq on ২৯/৫/১৯
"""

from sol_factory.base.serializers.domain_entity_serializer import DomainEntitySerializer
from sol_factory.products.models import Product
from sol_factory.products.serializers import ProductIconSerializer
from sol_factory.users.serializers import ConsoleUserGETSerializer

__author__ = "Shakib"


class ProductGETSerializer(DomainEntitySerializer):
    supplier = ConsoleUserGETSerializer(required=False)
    icons = ProductIconSerializer(many=True, required=False)

    class Meta(DomainEntitySerializer.Meta):
        model = Product
        fields = [
            'name', 'supplier', 'description', 'keyword', 'icons', 'is_new', 'id'
        ]
