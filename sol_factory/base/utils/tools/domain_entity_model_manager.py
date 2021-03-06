"""
    Created by tareq on ২/৭/১৯
"""
from django.db.models import Manager, Q

__author__ = "Tareq"


class DomainEntityModelManager(Manager):
    _filter = None
    _exclude = None

    def __init__(self, *args, filter=None, exclude=None, **kwargs):
        super().__init__(*args, **kwargs)
        self._filter = filter
        self._exclude = exclude

    def get_queryset(self, *args, **kwargs):
        queryset = super(DomainEntityModelManager, self).get_queryset()
        if self._filter:
            queryset = queryset.filter(Q(**self._filter))
        if self._exclude:
            queryset = queryset.exclude(Q(**self._exclude))
        return queryset
