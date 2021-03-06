from rest_framework.permissions import IsAuthenticatedOrReadOnly

from sol_factory.base.views import DomainEntityViewSet
from sol_factory.products.models import ProductAttribute
from sol_factory.products.serializers import ProductAttributeSerializer

__author__ = "Shakib"


class ProductCategoryAttributeViewSet(DomainEntityViewSet):
    serializer_class = ProductAttributeSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = ProductAttribute.objects.all()

    def get_queryset(self):
        queryset = super(ProductCategoryAttributeViewSet, self).get_queryset()
        category_id = self.request.GET.get('category', None)
        if category_id is not None:
            category_id = int(category_id)
            queryset = queryset.filter(category_attributes__product_category=category_id)
        return queryset
