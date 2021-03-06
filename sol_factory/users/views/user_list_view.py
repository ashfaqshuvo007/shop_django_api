"""
    Created by tareq on ১৪/৬/১৯
"""
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import AllowAny

from sol_factory.users.models import ConsoleUser
from sol_factory.users.serializers import ConsoleUserSerializer

__author__ = "Tareq"


class ConsoleUserListView(ListCreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ConsoleUserSerializer
    queryset = ConsoleUser.objects.all()
