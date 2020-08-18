from django.conf.urls import url
from django.urls import path, include

from .views import currency_list


urlpatterns = [
    path('exchange/', currency_list, name="currency-list"),
]