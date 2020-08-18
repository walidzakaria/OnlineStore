from requests import Response
from rest_framework.decorators import action, api_view
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


from .serializers import CategorySerializer, SubCategorySerializer, ProductSerializer
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
    List all sub categories
    """
    if request.method == 'GET':
        if lang == 'EN':
            sub_categories = SubCategory.objects.order_by('name').all()
        else:
            sub_categories = SubCategory.objects.order_by('name_ar').all()
        serializer = SubCategorySerializer(sub_categories, many=True)
        return Response(serializer.data)


@api_view(['GET', ])
def slider_product_list(request, lang):
    """
    List the slider products
    """
    if request.method == 'GET':
        slider_products = Product.objects.filter(slider=True).all()
        serializer = ProductSerializer(slider_products, many=True, context={'lang': lang})
        return Response(serializer.data)


@api_view(['GET', ])
def subcategory_product_list(request, lang, subcategory_id):
    """
    List the the products filtered by a sub-category
    """
    if request.method == 'GET':

        subcategory_products = Product.objects.filter(sub_category=subcategory_id).all()
        serializer = ProductSerializer(subcategory_products, many=True, context={'lang': lang})
        return Response(serializer.data)


@api_view(['GET', ])
def category_product_list(request, lang, category_id):
    """
    List the the products filtered by a category
    """
    if request.method == 'GET':

        category_products = Product.objects.filter(sub_category__category=category_id).all()
        serializer = ProductSerializer(category_products, many=True, context={'lang': lang})
        return Response(serializer.data)


@api_view(['GET', ])
def search_product_list(request, lang):
    """
    List the the products filtered by a category
    """
    if request.method == 'GET':

        category_products = Product.objects.filter(sub_category__category=category_id).all()
        serializer = ProductSerializer(category_products, many=True, context={'lang': lang})
        return Response(serializer.data)
