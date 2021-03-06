"""
    Created by tareq on ১৪/৬/১৯
"""
from rest_framework.permissions import AllowAny

from sol_factory.base.views import DomainEntityViewSet
from sol_factory.users.models import ConsoleUser
from sol_factory.users.serializers import ConsoleUserSerializer

__author__ = "Tareq"


class ConsoleUserViewSet(DomainEntityViewSet):
    permission_classes = (AllowAny,)
    serializer_class = ConsoleUserSerializer
    queryset = ConsoleUser.objects.all()
