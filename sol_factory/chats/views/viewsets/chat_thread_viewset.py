"""
    Created by tareq on 9/26/19
"""
from rest_framework.permissions import IsAuthenticated

from sol_factory.base.views.viewsets.domain_entity_viewset import DomainEntityViewSet
from sol_factory.chats.models import ChatThread
from sol_factory.chats.serializers.chat_thread_serializer import ChatThreadSerializer

__author__ = "Tareq"


class ChatThreadViewSet(DomainEntityViewSet):
    serializer_class = ChatThreadSerializer
    permission_classes = (IsAuthenticated,)
    queryset = ChatThread.objects.all()

    def get_queryset(self):
        queryset = super(ChatThreadViewSet, self).get_queryset()
        queryset = queryset.filter(thread_chat_inboxes__user=self.request.user)
        return queryset
