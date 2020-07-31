from rest_framework import serializers

from .models import UserAddress, Purchase, OrderItems
from apps.authapp.models import User


class UserAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAddress
        fields = '__all__'
