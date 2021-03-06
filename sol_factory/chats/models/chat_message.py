"""
    Created by tareq on ১/১০/১৯
"""
from django.db.models import ForeignKey, PROTECT, TextField, PositiveSmallIntegerField

from sol_factory.base.models import DomainEntity
from sol_factory.chats.enums.chat_message_status_enum import ChatMessageStatusEnum

__author__ = "Tareq"


class ChatMessage(DomainEntity):
    chat_inbox = ForeignKey('chats.ChatInbox', on_delete=PROTECT, related_name='inbox_chat_messages')
    sent_by = ForeignKey('users.ConsoleUser', on_delete=PROTECT, related_name='user_sent_messages')
    status = PositiveSmallIntegerField(default=ChatMessageStatusEnum.Unseen.value)
    text = TextField(blank=True)

    class Meta:
        app_label = 'chats'
