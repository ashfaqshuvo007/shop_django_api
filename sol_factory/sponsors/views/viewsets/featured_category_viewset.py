# Created by shamilsakib at 10/19/19
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from sol_factory.base.views.viewsets.domain_entity_viewset import DomainEntityViewSet
from sol_factory.sponsors.models import FeaturedCategory
from sol_factory.sponsors.serializers.featured_category_serializer import FeaturedCategorySerializer


class FeaturedCategoryViewSet(DomainEntityViewSet):
    serializer_class = FeaturedCategorySerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = FeaturedCategory.objects.all()

    def __init__(self, **kwargs):
        super(FeaturedCategoryViewSet, self).__init__(**kwargs)
        self.sort_by = 'name'

    def get_queryset(self):
        queryset = super(FeaturedCategoryViewSet, self).get_queryset()
        return queryset
