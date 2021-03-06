"""
    Created by tareq on ৩০/৯/১৯
"""
from django.db import transaction
from rest_framework.fields import SerializerMethodField

from sol_factory.base.serializers.domain_entity_serializer import DomainEntitySerializer
from sol_factory.chats.models import ChatInbox, ChatThread
from sol_factory.orders.models import Order
from sol_factory.products.serializers.product_breakdown_serializer import ProductBreakdownGETSerializer

__author__ = "Tareq"


class OrderGETSerializer(DomainEntitySerializer):
    product_breakdown = ProductBreakdownGETSerializer()
    thread = SerializerMethodField()

    def get_thread(self, instance):
        try:
            return instance.chatthread.pk
        except:
            return None

    class Meta(DomainEntitySerializer.Meta):
        model = Order
        fields = [
            'id', 'tsync_id', 'status', 'product_breakdown', 'buyer', 'thread',
            'quantity', 'unit_price', 'discount', 'total_price',
            'order_initiate_time', 'order_confirm_time', 'order_delivery_time', 'order_receive_time'
        ]


class OrderSerializer(DomainEntitySerializer):

    def create(self, validated_data):
        with transaction.atomic():
            validated_data['supplier'] = validated_data['product_breakdown'].product.supplier
            self.instance = super(OrderSerializer, self).create(validated_data=validated_data)

            thread, created = ChatThread.objects.get_or_create(reference_order_id=self.instance.pk)
            for participant in [self.instance.buyer_id, self.instance.supplier_id]:
                ChatInbox.objects.get_or_create(chat_thread_id=thread.pk, user_id=participant)
            return self.instance

    class Meta(DomainEntitySerializer.Meta):
        model = Order
        fields = [
            'id', 'tsync_id', 'status', 'product_breakdown', 'buyer', 'quantity', 'unit_price', 'discount',
            'total_price', 'order_initiate_time', 'order_confirm_time', 'order_delivery_time', 'order_receive_time'
        ]
