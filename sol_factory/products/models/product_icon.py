"""
    Created by tareq on ৫/৭/১৯
"""
from django.db.models import ImageField, IntegerField, TextField

from sol_factory.base.models import DomainEntity, FileObject

__author__ = "Tareq"


class ProductIcon(FileObject):

    class Meta:
        proxy=True
        app_label = 'products'

    def __str__(self):
        return "icon {} ({})".format(self.order, self.url)
