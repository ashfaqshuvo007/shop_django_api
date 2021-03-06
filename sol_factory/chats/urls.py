"""
    Created by tareq on ২৮/৬/১৯
"""

from django.urls import path, include
from rest_framework import routers

from sol_factory.chats.views.viewsets.chat_inbox_viewset import ChatInboxViewSet
from sol_factory.chats.views.viewsets.chat_message_viewset import ChatMessageViewSet
from sol_factory.chats.views.viewsets.chat_thread_viewset import ChatThreadViewSet

__author__ = "Tareq"

router = routers.DefaultRouter()
router.register(r'threads', ChatThreadViewSet)
router.register(r'inboxes', ChatInboxViewSet)
router.register(r'messages', ChatMessageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
