"""
    Created by tareq on ২/১০/১৯
"""
from sol_factory.base.serializers.domain_entity_serializer import DomainEntitySerializer
from sol_factory.chats.models import ChatInbox

__author__ = "Tareq"


class ChatInboxSerializer(DomainEntitySerializer):
    class Meta:
        model = ChatInbox
        fields = [
            'id', 'tsync_id', 'chat_thread', 'user'
        ]
