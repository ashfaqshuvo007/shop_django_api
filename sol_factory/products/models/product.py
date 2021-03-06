"""
    Created by tareq on ২৪/৫/১৯
"""
from datetime import timedelta
from math import ceil

from django.db.models import TextField, ForeignKey, CASCADE, ManyToManyField, DecimalField, IntegerField, PROTECT, \
    FloatField
from django.utils import timezone

from sol_factory.base.configs.business_logic_constants import NEW_PRODUCT_DAY_COUNT
from sol_factory.base.models.domain_entity import DomainEntity
from sol_factory.products.models import ProductAttributeValue

__author__ = "Tareq"


class Product(DomainEntity):
    supplier = ForeignKey('users.ConsoleUser', null=True, on_delete=PROTECT, related_name='supplier_products')
    category = ForeignKey('products.ProductCategory', null=True, on_delete=CASCADE)
    description = TextField(blank=True)
    keyword = TextField(blank=True, null=True, default=None)
    icons = ManyToManyField('products.ProductIcon')
    selling_price = FloatField(default=0)
    discount_amount = FloatField(default=0)
    stock_quantity = IntegerField(default=0)

    class Meta:
        app_label = 'products'

    @property
    def is_new(self):
        return self.date_created > (timezone.now() - timedelta(days=NEW_PRODUCT_DAY_COUNT))

    @property
    def original_price(self):
        return self.selling_price + self.discount_amount

    @property
    def discount_percent(self):
        try:
            return ceil(100.0 * float(self.discount_amount / (self.original_price)))
        except:
            return 0

    @classmethod
    def get_dependent_field_list(cls):
        return ['product_breakdowns', 'icons']

    @classmethod
    def get_products_by_attributes(cls, queryset=None, attribute_filters=[]):
        """
        This method will returd a queryset of products which contain certain values of attributes
        :param queryset: a queryset of product model
        :param attribute_filters: a list of attributes filter. In format: [{attribute: <pk>, value: <value>, relation: <relation>}]
        :return: a queryset of products containing the attribute value
        """
        if not queryset:
            queryset = Product.objects.all()

        product_ids = []
        for filter in attribute_filters:
            attribute_id = filter['attribute']
            value = filter['value']
            attributed_product_ids = list(ProductAttributeValue.objects.filter(
                product_attribute_id=attribute_id, value__value=value).values_list('product_breakdown__product_id'))
            if product_ids:
                product_ids = product_ids.intersection(attributed_product_ids)
            else:
                product_ids = set(attributed_product_ids)

            # If we reach an empty set, we no longer need to look for other attributes.
            if not product_ids:
                return queryset.none()

        if product_ids:
            return queryset.filter(id__in=list(product_ids))
        return queryset
