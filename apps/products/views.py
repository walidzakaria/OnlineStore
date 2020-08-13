from requests import Response
from rest_framework.decorators import action, api_view
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


from .serializers import CategorySerializer, SubCategorySerializer
from .models import Brand, Category, SubCategory, Product


@api_view(['GET', ])
def category_list(request, lang):
    """
    List all main categories
    """
    if request.method == 'GET':
        if lang == 'EN':
            categories = Category.objects.order_by('name').all()
        else:
            categories = Category.objects.order_by('name_ar').all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)


@api_view(['GET', ])
def sub_category_list(request, lang):
    """
    List all main categories
    """
    if request.method == 'GET':
        if lang == 'EN':
            sub_categories = SubCategory.objects.order_by('name').all()
        else:
            sub_categories = SubCategory.objects.order_by('name_ar').all()
        serializer = SubCategorySerializer(sub_categories, many=True)
        return Response(serializer.data)

