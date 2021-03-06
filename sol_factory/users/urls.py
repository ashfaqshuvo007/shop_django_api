"""
    Created by tareq on ১৪/৬/১৯
"""
from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers

from sol_factory.users.views import UserVerificationView
from sol_factory.users.views.login_view import LoginView
from sol_factory.users.views.viewsets.profile_viewset import ProfileViewSet
from sol_factory.users.views.viewsets.user_viewset import ConsoleUserViewSet

__author__ = "Tareq"

router = routers.DefaultRouter()
router.register(r'profile', ProfileViewSet)
router.register(r'users', ConsoleUserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_auth.urls')),
    path('registration/', include('rest_auth.registration.urls')),
    url(r'^user-verification/(?P<verification_code>([a-zA-Z0-9-_]+))/$', UserVerificationView.as_view(),
        name="user_verification_view"),
    url(r'^login/$', LoginView.as_view(), name="user_login_view"),
]
