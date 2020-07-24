from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def index(request):
    date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    message = 'Server is live current time is'
    return Response(data=message + date, status=status.HTTP_200_OK)