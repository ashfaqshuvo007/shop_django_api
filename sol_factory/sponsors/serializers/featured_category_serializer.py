# Created by shamilsakib at 10/19/19
from sol_factory.base.serializers.domain_entity_serializer import DomainEntitySerializer
from sol_factory.products.serializers import ProductIconSerializer
from sol_factory.sponsors.models import FeaturedCategory


class FeaturedCategorySerializer(DomainEntitySerializer):
    icons = ProductIconSerializer(many=True, required=False)

    class Meta(DomainEntitySerializer.Meta):
        model = FeaturedCategory
        fields = DomainEntitySerializer.Meta.fields + [
            'id', 'tsync_id', 'category', 'icons', 'is_master', 'is_published'
        ]
