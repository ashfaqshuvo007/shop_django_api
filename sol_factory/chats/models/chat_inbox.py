"""
    Created by tareq on ১/১০/১৯
"""
from django.db.models import ForeignKey, PROTECT

from sol_factory.base.models import DomainEntity

__author__ = "Tareq"


class ChatInbox(DomainEntity):
    chat_thread = ForeignKey('chats.ChatThread', on_delete=PROTECT, related_name='thread_chat_inboxes')
    user = ForeignKey('users.ConsoleUser', on_delete=PROTECT, related_name='user_chat_inboxes')

    class Meta:
        app_label = 'chats'
