from django.contrib.postgres.fields import JSONField
from django.db import models

from sol_factory.base.models import DomainEntity
from sol_factory.products.enums.product_attribute_enum import ProductAttributeBehaviorEnum

"""
Possible attributes pluggable to product category.
For example: Rating, Size, Has inverter, Color - this are product attribute
Now while creating categories, user can pick attributes that is applicable for that category 
from a predefined list of Product Attribute supported by the system.
"""


class ProductAttribute(DomainEntity):
    # Casual name
    name = models.CharField(max_length=128, null=True, default=None)
    # Note if required - can be used as help text to elaborate to user the real meaning of this attribute
    purpose = models.TextField(max_length=512, null=True, blank=True, default=None)
    # Pick from static list of attribute behavior, that will be used specifically
    # to define various functions of this attribute
    behavior = models.CharField(max_length=64, choices=ProductAttributeBehaviorEnum.get_choices(),
                                null=True, blank=True, default=None)
    # Don't know how to define it yet, but this will surely help us in future
    # for different conditions or validations for different product attributes during searching/showing/etc.
    condition = JSONField(default=None, null=True)

    def __init__(self, *args, **kwargs):
        super(ProductAttribute, self).__init__(*args, **kwargs)

    def __str__(self):
        return f'{self.name} as ({self.behavior}): {self.purpose}'

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        super(ProductAttribute, self).save(force_insert, force_update, using, update_fields)

    @property
    def choice_text(self):
        return self.name

    class Meta(DomainEntity.Meta):
        app_label = 'products'
