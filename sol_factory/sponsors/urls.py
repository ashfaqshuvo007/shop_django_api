"""
    Created by tareq on ২৮/৬/১৯
"""

from django.urls import path, include
from rest_framework import routers

from sol_factory.sponsors.views.viewsets.featured_category_viewset import FeaturedCategoryViewSet

__author__ = "Tareq"

router = routers.DefaultRouter()
router.register(r'featured-categories', FeaturedCategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
