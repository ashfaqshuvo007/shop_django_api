"""
    Created by tareq on ৫/৭/১৯
"""
from rest_framework import serializers

from sol_factory.base.serializers.domain_entity_serializer import DomainEntitySerializer
from sol_factory.products.models import ProductIcon

__author__ = "Tareq"


class ProductIconSerializer(DomainEntitySerializer):

    def create(self, validated_data):
        instance = super(ProductIconSerializer, self).create(validated_data)
        try:
            instance.convert_pondfile_to_file(
                token=instance.token,
                request=self.context['request']
            )
        except:
            pass
        return instance

    def update(self, instance, validated_data):
        instance = super(ProductIconSerializer, self).update(instance, validated_data)
        try:
            instance.convert_pondfile_to_file(
                token=instance.token,
                request=self.context['request']
            )
        except:
            pass
        return instance

    class Meta(DomainEntitySerializer.Meta):
        model = ProductIcon
        fields = DomainEntitySerializer.Meta.fields + [
            'full_url', 'url', 'order', 'title', 'token'
        ]
