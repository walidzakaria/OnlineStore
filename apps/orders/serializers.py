from django.utils import timezone
from rest_framework import serializers

from .models import UserAddress, Order, OrderItems, Shipping
from ..currencies.models import Currency
from ..currencies.serializers import CurrencySerializer
from ..products.serializers import ProductSerializer


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


class UserAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAddress
        fields = '__all__'


class GetOrderSerializer(serializers.ModelSerializer):
    currency_code = serializers.CharField(read_only=True, source='currency.code')
    user_city = serializers.CharField(read_only=True, source='user_address.city.city')
    user_address = serializers.CharField(read_only=True, source='user_address.address')
    due_days = serializers.SerializerMethodField('get_due_days')

    def get_due_days(self, obj):
        if obj.status in ['Preparation', 'Delivery'] and obj.due_date:
            due_date = obj.due_date - timezone.now().date()
            return due_date.days
        else:
            return None

    class Meta:
        model = Order
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'


class OrderItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItems
        fields = '__all__'


class OrderDetailedSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = OrderItems
        fields = '__all__'
