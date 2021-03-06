"""
    Created by tareq on 9/26/19
"""
from rest_framework.permissions import IsAuthenticated

from sol_factory.base.views.viewsets.domain_entity_viewset import DomainEntityViewSet
from sol_factory.chats.configs.constants import CHAT_WINDOW_MESSAGE_COUNT
from sol_factory.chats.models import ChatMessage
from sol_factory.chats.serializers.chat_message_serializer import ChatMessageSerializer

__author__ = "Tareq"


class ChatMessageViewSet(DomainEntityViewSet):
    serializer_class = ChatMessageSerializer
    permission_classes = (IsAuthenticated,)
    queryset = ChatMessage.objects.all()

    def get_queryset(self):
        queryset = super(ChatMessageViewSet, self).get_queryset()
        queryset = queryset.filter(chat_inbox__user=self.request.user)

        chat_thread = self.request.query_params.get("chat_thread", None)
        if chat_thread:
            queryset = queryset.filter(chat_inbox__chat_thread_id=chat_thread)
        last_message = self.request.query_params.get("last_message", None)
        if last_message:
            queryset = queryset.filter(pk__lt=last_message)

        message_count = self.request.query_params.get("limit", CHAT_WINDOW_MESSAGE_COUNT)
        queryset = queryset.order_by("-pk")[:message_count]

        return queryset
