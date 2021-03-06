"""
    Created by tareq on ২৯/৯/১৯
"""
from django.db import transaction
from django.db.models import IntegerField, ForeignKey, PROTECT, DateTimeField, FloatField

from sol_factory.base.models import DomainEntity
from sol_factory.orders.enums.order_status_enum import OrderStatusEnum
from sol_factory.orders.models.order_version import OrderVersion

__author__ = "Tareq"


class Order(DomainEntity):
    status = IntegerField(default=OrderStatusEnum.Pending.value)
    product_breakdown = ForeignKey('products.ProductBreakdown', related_name='orders', null=True, on_delete=PROTECT)
    buyer = ForeignKey('users.ConsoleUser', related_name='buyer_orders', null=True, on_delete=PROTECT)
    supplier = ForeignKey('users.ConsoleUser', related_name='supplier_orders', null=True, on_delete=PROTECT)

    quantity = IntegerField(default=0)
    unit_price = FloatField(default=0)
    discount = FloatField(default=0)
    total_price = FloatField(default=0)

    order_initiate_time = DateTimeField(auto_now_add=True)
    order_confirm_time = DateTimeField(default=None, null=True)
    order_delivery_time = DateTimeField(default=None, null=True)
    order_receive_time = DateTimeField(default=None, null=True)

    class Meta:
        app_label = 'orders'

    def save(self, create_version=True, *args, **kwargs):
        with transaction.atomic():
            if self.product_breakdown_id:
                self.supplier_id = self.product_breakdown.product.supplier_id
            result = super(Order, self).save(*args, **kwargs)
            if create_version:
                _version = OrderVersion(reference_order_id=self.pk, json_body=self.to_json())
                _version.save()
            return result

    def to_json(self):
        return {
            'status': self.status,
            'product_breakdown': self.product_breakdown_id,
            'buyer': self.buyer_id,
            'supplier': self.supplier_id,
            'quantity': self.quantity,
            'unit_price': self.unit_price,
            'discount': self.discount,
            'total_price': self.total_price,
            'order_initiate_time': self.order_initiate_time.timestamp() if self.order_initiate_time else 0,
            'order_confirm_time': self.order_confirm_time.timestamp() if self.order_confirm_time else 0,
            'order_delivery_time': self.order_delivery_time.timestamp() if self.order_delivery_time else 0,
            'order_receive_time': self.order_receive_time.timestamp() if self.order_receive_time else 0,
        }
