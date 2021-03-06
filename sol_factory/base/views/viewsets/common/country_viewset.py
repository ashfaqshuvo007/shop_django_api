"""
    Created by sakib
"""
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from sol_factory.base.models import Country
from sol_factory.base.serializers.common.country_serializer import CountrySerializer
from sol_factory.base.views.viewsets.domain_entity_viewset import DomainEntityViewSet

__author__ = "Shakib"


class CountryViewSet(DomainEntityViewSet):
    serializer_class = CountrySerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Country.objects.all()

    def __init__(self, **kwargs):
        super(CountryViewSet, self).__init__(**kwargs)
        self.sort_by = 'name'

    def get_queryset(self):
        queryset = super(CountryViewSet, self).get_queryset()
        return queryset
