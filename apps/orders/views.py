from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import UserAddress
from .serializers import UserAddressSerializer


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
    Update or delete a code snippet.
    """

    try:
        user_address = UserAddress.objects.get(pk=pk)
    except UserAddress.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    print(user_address.user)
    print(request.user)
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