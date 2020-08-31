from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from drf_multiple_model.views import ObjectMultipleModelAPIView

from .models import UserAddress, Order, Shipping
from .serializers import UserAddressSerializer, OrderSerializer, OrderItemsSerializer, ShippingSerializer
from ..currencies.models import Currency
from ..products.models import Category


@api_view(['GET', ])
def shipping_list(request, currency_id, lang):
    """
    List shipping details based on given lang & curr
    """
    if request.method == 'GET':
        if not Currency.exists(currency_id):
            return Response(data={"message": "currency doesn't exist"}, status=status.HTTP_404_NOT_FOUND)

        if lang == 'en':
            shipping = Shipping.objects.order_by('city').all()
        else:
            shipping = Shipping.objects.order_by('city_ar').all()

        serializer = ShippingSerializer(shipping,
                                        context={'lang': lang, 'curr': currency_id},
                                        many=True)

        return Response(serializer.data)


@api_view(['GET', ])
def shipping_detail(request, city_id, currency_id, lang):
    """
    List shipping details based on given lang & curr
    """
    if request.method == 'GET':
        if not Currency.exists(currency_id):
            return Response(data={"message": "currency doesn't exist"}, status=status.HTTP_404_NOT_FOUND)

        shipping = Shipping.objects.filter(id=city_id).first()

        if not shipping:
            return Response(data={"message": "city doesn't exist"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ShippingSerializer(shipping,
                                        context={'lang': lang, 'curr': currency_id},
                                        many=False)

        return Response(serializer.data)


@api_view(['GET', 'POST', ])
@permission_classes([IsAuthenticated])
def user_address_list(request):
    """
    List logged user addresses or create a new address
    """
    if request.method == 'GET':
        user = request.user
        user_addresses = UserAddress.objects.filter(user=user)
        serializer = UserAddressSerializer(user_addresses, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        request.data['user'] = request.user.id
        print(request.data)
        serializer = UserAddressSerializer(data=request.data)
        serializer.user = request.user

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'DELETE', ])
@permission_classes([IsAuthenticated])
def user_address_detail(request, pk):
    """
    Update or delete a user address.
    """

    try:
        user_address = UserAddress.objects.get(pk=pk)
    except UserAddress.DoesNotExist:
        return Response(data={"message": "no address found with this id"}, status=status.HTTP_404_NOT_FOUND)

    if user_address.user != request.user:
        return Response(data={"message": "invalid user to update this address"},
                        status=status.HTTP_401_UNAUTHORIZED)

    if request.method == 'PUT':
        user = request.user
        request.data['user'] = user.id
        serializer = UserAddressSerializer(user_address, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user_address.delete()
        return Response(data={"message": "deleted"}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST', ])
@permission_classes([IsAuthenticated])
def user_orders(request):
    """
    List all logged user orders, or create an order
    """
    if request.method == 'GET':
        user = request.user
        orders = Order.objects.filter(client=user)

        serializer = OrderSerializer(orders, many=True)
        return Response(
            {
                "count": orders.count(),
                "data": serializer.data
            })

    if request.method == 'POST':
        request.data[0]['client'] = request.user.id
        request.data[0]['created_by'] = request.user.id
        request.data[0]['updated_by'] = request.user.id
        request.data[0]['number_of_items'] = 0
        request.data[0]['due_amount'] = 0

        order_serializer = OrderSerializer(data=request.data[0])
        if order_serializer.is_valid():
            new_order = order_serializer.save()

            for i in request.data[1]:
                i['order'] = new_order.id
                i['product_value'] = 0
            order_item_serializer = OrderItemsSerializer(data=request.data[1], many=True)
            if order_item_serializer.is_valid():
                order_items = order_item_serializer.save()
                for order_item in order_items:
                    order_item.calculate()
                new_order.calculate()
            else:
                return Response(order_item_serializer.errors,
                                status=status.HTTP_400_BAD_REQUEST)

            return Response(order_serializer.data,
                            status=status.HTTP_201_CREATED)

        return Response(order_serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)
