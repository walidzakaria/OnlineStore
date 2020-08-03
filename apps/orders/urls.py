from django.conf.urls import url
from django.urls import path, include

from apps.orders.views import user_address_list, user_address_detail, user_orders

urlpatterns = [
    url('user-addresses/$', user_address_list, name="user-address-list"),
    url('user-addresses/(?P<pk>[0-9]+)$', user_address_detail, name="user-address-detail"),
    url('user-orders/$', user_orders, name="user-orders-list"),
]