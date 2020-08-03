from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from drf_multiple_model.views import ObjectMultipleModelAPIView

from .models import UserAddress, Order
from .serializers import UserAddressSerializer, OrderSerializer, OrderItemsSerializer


@api_view(['GET', 'POST', ])
@permission_classes([IsAuthenticated])
def user_address_list(request):
    """
    List all logged user addresses or create a new address
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
        return Response(status=status.HTTP_404_NOT_FOUND)

    if user_address.user != request.user:
        return Response(status=status.HTTP_401_UNAUTHORIZED)

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
        return Response(status=status.HTTP_204_NO_CONTENT)


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
