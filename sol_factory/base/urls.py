"""
    Created by Shakib
"""

from django.urls import path, include
from rest_framework import routers

from sol_factory.base.views.viewsets.common.country_viewset import CountryViewSet

__author__ = "Shakib"

router = routers.DefaultRouter()
router.register(r'country', CountryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
