from django.conf.urls import url
from django.urls import path, include

from apps.orders.views import (
    user_address_list, user_address_detail, user_orders_list, shipping_list,
    shipping_detail, user_order_post, user_order_detail
)

urlpatterns = [
    url('user-addresses/$', user_address_list, name="user-address-list"),
    path('user-addresses/<int:user_address_id>', user_address_detail, name="user-address-detail"),
    url('user-orders/$', user_orders_list, name="user-orders-list"),
    path('shipping/<int:currency_id>/<str:lang>', shipping_list, name="shipping-list"),
    path('shipping/<int:city_id>/<int:currency_id>/<str:lang>',
         shipping_detail, name="shipping-detail"),
    path('user-order-create/', user_order_post, name='user-order-create'),
    path('user-orders/<int:order_id>/<str:lang>', user_order_detail, name='user-order-detail'),
]