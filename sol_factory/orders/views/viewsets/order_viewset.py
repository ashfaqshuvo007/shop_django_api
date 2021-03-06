"""
    Created by tareq on 9/26/19
"""
from rest_framework.permissions import IsAuthenticated

from sol_factory.base.views.viewsets.domain_entity_viewset import DomainEntityViewSet
from sol_factory.orders.models import Order
from sol_factory.orders.serializers.order_serializer import OrderSerializer, OrderGETSerializer

__author__ = "Tareq"


class OrderViewSet(DomainEntityViewSet):
    serializer_class = OrderSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Order.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return OrderGETSerializer
        return OrderSerializer

    def get_queryset(self):
        queryset = super(OrderViewSet, self).get_queryset()
        queryset = queryset.filter(buyer=self.request.user) | queryset.filter(supplier=self.request.user)
        return queryset
