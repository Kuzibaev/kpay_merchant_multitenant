import datetime

from rest_framework import serializers

from orders import models as order_models
from utility.datetime import now


class OrderItemSerializerCreate(serializers.ModelSerializer):
    date = serializers.DateTimeField(default=now())
    monthly_payment = serializers.FloatField(default=0.0)
    remained_payment = serializers.FloatField(default=0.0)

    class Meta:
        model = order_models.OrderItem
        fields = (
            'date',
            'monthly_payment',
            'remained_payment'
        )


class OrderProductSerializerCreate(serializers.ModelSerializer):
    class Meta:
        model = order_models.OrderProduct
        fields = (
            'serial_number',
            'product',
            'quantity'
        )


class OrderSerializerCreate(serializers.ModelSerializer):
    total_price = serializers.FloatField(default=0.0)
    first_payment = serializers.FloatField(default=0.0)
    left_payment = serializers.FloatField(default=0.0)
    products = OrderProductSerializerCreate(many=True, read_only=True)
    order_items = OrderItemSerializerCreate(many=True, read_only=True)

    class Meta:
        model = order_models.Order
        fields = (
            'buyer',
            'merchant',
            'payment_date',
            'total_price',
            'first_payment',
            'left_payment',
            'interval',
            'products',
            'order_items'
        )


class OrderProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = order_models.OrderProduct
        fields = "__all__"


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = order_models.OrderItem
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    products = OrderProductSerializer(many=True)
    order_items = OrderItemSerializer(many=True)

    class Meta:
        model = order_models.Order
        fields = "__all__"


class MainSerializer(serializers.Serializer):
    total_sum = serializers.FloatField(default=0.0)
    total_sum_paid = serializers.FloatField(default=0.0)
    total_sum_not_paid = serializers.FloatField(default=0.0)
    total_sum_must_pay_today = serializers.FloatField(default=0.0)
    total_sum_month_year = serializers.FloatField(default=0.0)
