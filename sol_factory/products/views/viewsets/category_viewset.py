"""
    Created by tareq on 9/26/19
"""
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from sol_factory.base.views.viewsets.domain_entity_viewset import DomainEntityViewSet
from sol_factory.products.models import ProductCategory
from sol_factory.products.serializers import ProductCategorySerializer

__author__ = "Tareq"


class CategoryViewSet(DomainEntityViewSet):
    serializer_class = ProductCategorySerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = ProductCategory.objects.all()

    def __init__(self, **kwargs):
        super(CategoryViewSet, self).__init__(**kwargs)
        self.sort_by = 'name'

    def get_queryset(self):
        queryset = super(CategoryViewSet, self).get_queryset()
        parent_id = self.request.GET.get('parent', None)
        if parent_id is not None:
            parent_id = int(parent_id)
            queryset = queryset.filter(parent_id=parent_id if parent_id else None)
        return queryset
