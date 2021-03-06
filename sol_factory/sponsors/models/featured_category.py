# Created by shamilsakib at 10/19/19
from django.db.models import ForeignKey, SET_NULL, ManyToManyField, BooleanField

from sol_factory.base.models.domain_entity import DomainEntity


class FeaturedCategory(DomainEntity):
    category = ForeignKey('products.ProductCategory', null=True, on_delete=SET_NULL, blank=True)
    icons = ManyToManyField('products.ProductIcon')
    is_master = BooleanField(default=False)
    is_published = BooleanField(default=False)

    class Meta:
        app_label = 'sponsors'

    def __str__(self):
        prefix = ''
        if self.category:
            prefix = "Featured: {} > ".format(str(self.category))
        return prefix + str(self.is_master)
