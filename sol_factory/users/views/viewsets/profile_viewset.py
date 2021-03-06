"""
    Created by tareq on ২০/৯/১৯
"""
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from sol_factory.base.views.viewsets.domain_entity_viewset import DomainEntityViewSet
from sol_factory.users.models import UserProfileInfo
from sol_factory.users.serializers.profile import ProfileInfoSerializer

__author__ = "Tareq"


class ProfileViewSet(DomainEntityViewSet):
    serializer_class = ProfileInfoSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = UserProfileInfo.objects.all()

    def get_queryset(self):
        return self.queryset.filter(consoleuser=self.request.user)
