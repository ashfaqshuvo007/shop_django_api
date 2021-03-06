"""
    Created by tareq on ২/১০/১৯
"""
from django.db import transaction
from rest_framework.fields import SerializerMethodField

from sol_factory.base.serializers.domain_entity_serializer import DomainEntitySerializer
from sol_factory.chats.models import ChatThread, ChatInbox
from sol_factory.chats.serializers.chat_inbox_serializer import ChatInboxSerializer

__author__ = "Tareq"


class ChatThreadSerializer(DomainEntitySerializer):
    thread_chat_inboxes = ChatInboxSerializer(many=True, read_only=True)
    participants = SerializerMethodField()

    def get_participants(self, obj):
        return list(obj.thread_chat_inboxes.values_list('user_id', flat=True))

    def create(self, validated_data):
        with transaction.atomic():
            self.instance = super(ChatThreadSerializer, self).create(validated_data=validated_data)

            for participant in self.initial_data.get('participants', []):
                ChatInbox.objects.get_or_create(chat_thread_id=self.instance.pk, user_id=participant)
            return self.instance

    class Meta:
        model = ChatThread
        fields = [
            'id', 'tsync_id', 'reference_order', 'last_updated', 'date_created', 'thread_chat_inboxes', 'participants'
        ]
