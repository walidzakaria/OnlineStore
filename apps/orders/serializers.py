from rest_framework import serializers

from .models import UserAddress, Order, OrderItems, Shipping
from ..currencies.models import Currency


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


class ShippingSerializer(serializers.ModelSerializer):
    city_name = serializers.SerializerMethodField('get_city')
    fees = serializers.SerializerMethodField('get_fees')

    def get_city(self, obj):
        lang = self.context.get('lang')
        if lang == 'en':
            return obj.city
        else:
            return obj.city_ar

    def get_fees(self, obj):
        currency_id = self.context.get("curr")
        currency = Currency.objects.get(pk=currency_id)
        return obj.shipping_fees * currency.rate

    class Meta:
        model = Shipping
        fields = ('id', 'city_name', 'fees', )
