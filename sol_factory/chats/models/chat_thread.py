"""
    Created by tareq on ১/১০/১৯
"""
from django.db.models import OneToOneField, PROTECT

from sol_factory.base.models import DomainEntity
from sol_factory.chats.configs.constants import CHAT_WINDOW_MESSAGE_COUNT

__author__ = "Tareq"


class ChatThread(DomainEntity):
    reference_order = OneToOneField('orders.Order', null=True, on_delete=PROTECT)

    class Meta:
        app_label = 'chats'

    def get_chat_messages(self, offset=0, limit=CHAT_WINDOW_MESSAGE_COUNT):
        return self.inbox_chat_messages.order_by('-pk')[offset:offset + limit]

    def get_chat_messages_older_than(self, last=None, limit=CHAT_WINDOW_MESSAGE_COUNT):
        if last:
            return self.inbox_chat_messages.filter(pk__lt=last).order_by('-pk')[:limit]
        return self.inbox_chat_messages.order_by('-pk')[:limit]
