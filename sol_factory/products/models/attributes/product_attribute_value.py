from django.db.models import ForeignKey, CASCADE

from sol_factory.base.models import DomainEntity
from sol_factory.products.models.attributes.abstract_attribute_value import AbstractAttributeValue

"""
This is a M2M Through field of Product-ProductAttribute relation, that will keep the values.
"""


class ProductAttributeValue(AbstractAttributeValue):
    product_breakdown = ForeignKey(
        'products.ProductBreakdown', null=True, on_delete=CASCADE, related_name='product_attributes')

    def __str__(self):
        return f'{self.product_breakdown.product}\'s {self.product_attribute.name}: {self.value}'

    class Meta(DomainEntity.Meta):
        app_label = 'products'
