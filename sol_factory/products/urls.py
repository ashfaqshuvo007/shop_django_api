"""
    Created by tareq on ২৮/৬/১৯
"""

from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers

from sol_factory.products.views.product_category_attribute_view import ProductCategoryAttributeViewSet
from sol_factory.products.views.viewsets.category_viewset import CategoryViewSet
from sol_factory.products.views.viewsets.product_viewset import ProductViewSet

__author__ = "Tareq"

router = routers.DefaultRouter()
router.register(r'product', ProductViewSet)
router.register(r'category', CategoryViewSet)
router.register(r'attribute', ProductCategoryAttributeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
