from rest_framework import serializers

from .models import UserAddress, Order, OrderItems


class UserAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAddress
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class OrderItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItems
        fields = '__all__'


class TestSerializer(serializers.ModelSerializer):
    order = OrderItemsSerializer()

    class Meta:
        model = OrderItems
        fields = '__all__'

    def create(self, validated_data):
        profile_data = validated_data.pop('order')
        new_order = Order.objects.create(**validated_data)
        OrderItems.objects.create(order=new_order, **profile_data)
        return new_order
