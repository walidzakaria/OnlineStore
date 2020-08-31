from django.conf.urls import url
from django.urls import path, include

from apps.orders.views import (
    user_address_list, user_address_detail, user_orders, shipping_list,
    shipping_detail
)

urlpatterns = [
    url('user-addresses/$', user_address_list, name="user-address-list"),
    url('user-addresses/(?P<pk>[0-9]+)$', user_address_detail, name="user-address-detail"),
    url('user-orders/$', user_orders, name="user-orders-list"),
    path('shipping/<int:currency_id>/<str:lang>', shipping_list, name="shipping-list"),
    path('shipping/<int:city_id>/<int:currency_id>/<str:lang>',
         shipping_detail, name="shipping-detail"),
]