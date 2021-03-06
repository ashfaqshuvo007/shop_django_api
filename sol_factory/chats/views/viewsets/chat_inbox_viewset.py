"""
    Created by tareq on 9/26/19
"""
from rest_framework.permissions import IsAuthenticated

from sol_factory.base.views.viewsets.domain_entity_viewset import DomainEntityViewSet
from sol_factory.chats.models import ChatInbox
from sol_factory.chats.serializers.chat_inbox_serializer import ChatInboxSerializer

__author__ = "Tareq"


class ChatInboxViewSet(DomainEntityViewSet):
    serializer_class = ChatInboxSerializer
    permission_classes = (IsAuthenticated,)
    queryset = ChatInbox.objects.all()

    def get_queryset(self):
        queryset = super(ChatInboxViewSet, self).get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset
