from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import ExchangeRate, Currency
from .serializers import CurrencySerializer


# Create your views here.
@api_view(['GET', ])
def currency_list(request):
    """
    List last currency with exchange rates
    """
    if request.method == 'GET':
        currencies = Currency.objects.all()
        serializer = CurrencySerializer(currencies, many=True)
        return Response(serializer.data)

