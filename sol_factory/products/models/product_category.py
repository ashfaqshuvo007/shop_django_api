"""
    Created by tareq on ২৪/৫/১৯
"""
from django.db.models import TextField, ForeignKey, SET_NULL, ManyToManyField

from sol_factory.base.models.domain_entity import DomainEntity

__author__ = "Tareq"


class ProductCategory(DomainEntity):
    parent = ForeignKey('self', null=True, on_delete=SET_NULL, blank=True)
    description = TextField(blank=True)
    icons = ManyToManyField('products.ProductIcon')

    attributes = ManyToManyField(
        'products.ProductAttribute', through='products.ProductCategoryAttribute',
        through_fields=('product_category', 'product_attribute'), blank=True)

    class Meta:
        app_label = 'products'

    def __str__(self):
        prefix = ''
        if self.parent:
            prefix = "{} > ".format(str(self.parent))
        return prefix + self.name

    def parent_category(self):
        return self.parent

    def number_of_products(self):
        from sol_factory.products.models.product import Product
        return Product.objects.filter(category_id=self.pk).count()

    @classmethod
    def include_sub_categories(cls, parent_id=None):
        categories = ProductCategory.objects.filter(parent_id=parent_id)
        sub_categories = []
        for category in categories:
            sub_categories.append(category.pk)
            sub_categories += cls.include_sub_categories(parent_id=category.pk)
        return [parent_id] + sub_categories
