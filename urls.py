"""sol_factory URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include
from django.urls import path
from rest_framework import routers

router = routers.DefaultRouter()

urlpatterns = [
    # url(r'', include(router.urls)),
    path('admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^base/', include('sol_factory.base.urls')),
    url(r'^users/', include('sol_factory.users.urls')),
    url(r'^products/', include('sol_factory.products.urls')),
    url(r'^sponsors/', include('sol_factory.sponsors.urls')),
    url(r'^orders/', include('sol_factory.orders.urls')),
    url(r'^chats/', include('sol_factory.chats.urls')),
    url(r'^media-uploads/', include('django_drf_filepond.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
