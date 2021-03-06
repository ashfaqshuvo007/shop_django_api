"""
    Created by tareq on 8/16/19
"""
from django.contrib.postgres.fields import JSONField
from django.db.models import ForeignKey, PROTECT, TextField

from sol_factory.base.models import DomainEntity

__author__ = "Tareq"


class AbstractAttributeValue(DomainEntity):
    category_attribute = ForeignKey(
        'products.ProductCategoryAttribute', verbose_name='Attribute', on_delete=PROTECT,
        default=None, null=True)
    # Cache attribute here, so multiple join is not required to get the value of attribute
    product_attribute = ForeignKey('products.ProductAttribute', null=True, on_delete=PROTECT)
    note = TextField(default=None, null=True, blank=True)
    # Format: {"value": "XL"} or {"value": true} or {"value": 5.25} or {"value": 2}
    # This is very important. JSONField will help us to make queries
    # Value cam ne string/boolean/number mostly. Now it is not possible to define three field rather keep one JSONField
    # We will keep the value as the mentioned formats above, and probably based on behavior or attribute
    # we can write different type of queries on "value" key and get result. Not 100% sure yet if it will work though.
    value = JSONField(default=None, null=True, blank=True)

    class Meta:
        app_label = 'products'
        abstract = True

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self.category_attribute and not self.product_attribute:
            self.product_attribute_id = self.category_attribute.product_attribute_id
        return super(AbstractAttributeValue, self).save(
            force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields)
