"""
    Created by tareq on ২/১০/১৯
"""
from django.db import transaction
from rest_framework.fields import SerializerMethodField, IntegerField

from sol_factory.base.serializers.domain_entity_serializer import DomainEntitySerializer
from sol_factory.chats.models import ChatMessage, ChatThread

__author__ = "Tareq"


class ChatMessageSerializer(DomainEntitySerializer):
    chat_thread = SerializerMethodField()
    sent_by = SerializerMethodField(required=False)

    def get_chat_thread(self, obj):
        return obj.chat_inbox.chat_thread_id

    def get_sent_by(self, obj):
        return obj.sent_by_id

    def create(self, validated_data):
        with transaction.atomic():
            validated_data['sent_by'] = self.context['request'].user
            thread = ChatThread.objects.get(pk=self.initial_data.get('chat_thread', None))
            inbox = thread.thread_chat_inboxes.get(user=validated_data['sent_by'])
            inbox_counterparts = thread.thread_chat_inboxes.exclude(user=validated_data['sent_by'])
            validated_data['chat_inbox'] = inbox
            self.instance = super(ChatMessageSerializer, self).create(validated_data=validated_data)

            for counterpart in inbox_counterparts:
                ChatMessage.objects.create(
                    text=self.instance.text, chat_inbox=counterpart, sent_by=self.instance.sent_by)

            return self.instance

    class Meta:
        model = ChatMessage
        fields = [
            'id', 'tsync_id', 'text', 'chat_thread', 'sent_by'
        ]
