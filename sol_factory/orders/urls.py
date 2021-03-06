"""
    Created by tareq on ২৮/৬/১৯
"""

from django.urls import path, include
from rest_framework import routers

from sol_factory.orders.views.viewsets.order_viewset import OrderViewSet

__author__ = "Tareq"

router = routers.DefaultRouter()
router.register(r'order', OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
