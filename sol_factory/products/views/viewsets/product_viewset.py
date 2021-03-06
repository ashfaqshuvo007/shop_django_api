"""
    Created by tareq on 9/26/19
"""
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from sol_factory.base.views.viewsets.domain_entity_viewset import DomainEntityViewSet
from sol_factory.products.models import Product, ProductCategory
from sol_factory.products.serializers import ProductSerializer

__author__ = "Tareq"


class ProductViewSet(DomainEntityViewSet):
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Product.objects.all()

    def get_queryset(self):
        queryset = super(ProductViewSet, self).get_queryset()
        category_id = int(self.request.GET.get('category', 0))
        if category_id:
            categories = ProductCategory.include_sub_categories(parent_id=category_id)
            queryset = queryset.filter(category_id__in=categories)
        name = self.request.GET.get('name', None)
        if name:
            queryset = queryset.filter(name__icontains=name)
        return queryset
