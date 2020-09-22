# encoding=utf-8

from requests import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action, api_view
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from django.db.models import Q

from .serializers import CategorySerializer, SubCategorySerializer, ProductSerializer, SliderSerializer
from .models import Brand, Category, SubCategory, Product, Slider
from ..currencies.models import Currency


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
def slider_list(request, lang):
    """
    List the sliders
    """
    if request.method == 'GET':
        sliders = Slider.objects.filter(active=True). \
            filter(Q(lang='both') | Q(lang=lang)).all()
        serializer = SliderSerializer(sliders, many=True)
        return Response(serializer.data)


@api_view(['GET', ])
def subcategory_product_list(request, subcategory_id, currency_id, lang):
    """
    List the the products filtered by a sub-category in paginated view
    """
    if request.method == 'GET':
        paginator = PageNumberPagination()
        paginator.page_size = 10

        if not Currency.exists(currency_id):
            return Response(data={"message": "currency doesn't exist"}, status=status.HTTP_404_NOT_FOUND)

        subcategory_products = Product.objects.filter(
            sub_category=subcategory_id, active=True).all()
        result_page = paginator.paginate_queryset(subcategory_products, request)
        serializer = ProductSerializer(result_page, many=True, context={'lang': lang, 'curr': currency_id})
        return paginator.get_paginated_response(serializer.data)


@api_view(['GET', ])
def category_product_list(request, category_id, currency_id, lang):
    """
    List the the products filtered by a category in paginated view
    """
    if request.method == 'GET':
        if not Currency.exists(currency_id):
            return Response(data={"message": "currency doesn't exist"}, status=status.HTTP_404_NOT_FOUND)

        paginator = PageNumberPagination()
        paginator.page_size = 10
        category_products = Product.objects.filter(
            sub_category__category=category_id, active=True).all()
        result_page = paginator.paginate_queryset(category_products, request)
        serializer = ProductSerializer(result_page, many=True, context={'lang': lang, 'curr': currency_id})
        return paginator.get_paginated_response(serializer.data)


@api_view(['GET', ])
def trending_product_list(request, currency_id, lang):
    """
    List the the trending products filtered by a category in paginated view
    """
    if request.method == 'GET':
        if not Currency.exists(currency_id):
            return Response(data={"message": "currency doesn't exist"}, status=status.HTTP_404_NOT_FOUND)

        paginator = PageNumberPagination()
        paginator.page_size = 10
        trending_products = Product.objects.filter(balance__gt=0, active=True).all().order_by('-sold')
        result_page = paginator.paginate_queryset(trending_products, request)
        serializer = ProductSerializer(result_page, many=True, context={'lang': lang, 'curr': currency_id})
        return paginator.get_paginated_response(serializer.data)


@api_view(['GET', ])
def best_selling_product_list(request, currency_id, lang):
    """
    List the the best selling products filtered by a category in paginated view
    """
    if request.method == 'GET':
        if not Currency.exists(currency_id):
            return Response(data={"message": "currency doesn't exist"}, status=status.HTTP_404_NOT_FOUND)

        paginator = PageNumberPagination()
        paginator.page_size = 10
        best_selling_products = Product.objects.filter(balance__gt=0, active=True).all().order_by('-reduction')
        result_page = paginator.paginate_queryset(best_selling_products, request)
        serializer = ProductSerializer(result_page, many=True, context={'lang': lang, 'curr': currency_id})
        return paginator.get_paginated_response(serializer.data)


@api_view(['GET', ])
def new_arrival_product_list(request, currency_id, lang):
    """
    List the the products ordered from newest arrival to oldest in paginated view
    """
    if request.method == 'GET':
        if not Currency.exists(currency_id):
            return Response(data={"message": "currency doesn't exist"}, status=status.HTTP_404_NOT_FOUND)

        paginator = PageNumberPagination()
        paginator.page_size = 10
        recent_products = Product.objects.raw('''
            SELECT product.*
            FROM Products_Product product
            JOIN Orders_Purchase purchase ON product.id = purchase.product_id
            WHERE product.balance > 0
            AND product.active = True
            ORDER BY purchase.id DESC; 
            ''')
        result_page = paginator.paginate_queryset(recent_products, request)
        serializer = ProductSerializer(result_page, many=True, context={'lang': lang, 'curr': currency_id})
        return paginator.get_paginated_response(serializer.data)


@api_view(['GET', ])
def product_details(request, product_id, currency_id, lang):
    """
    Shows a selected products details
    """
    if request.method == 'GET':
        if not Currency.exists(currency_id):
            return Response(data={"message": "currency doesn't exist"}, status=status.HTTP_404_NOT_FOUND)

        product = Product.objects.filter(id=product_id).first()

        if not product:
            return Response(data={"message": "product not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ProductSerializer(product, many=False, context={'lang': lang, 'curr': currency_id})
        return Response(serializer.data)


class ApiProductList(ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        lang = self.kwargs.get('lang')
        currency_id = self.kwargs.get('currency_id')
        self.serializer_class.context = {'lang': lang, 'curr': currency_id}
        return Product.objects.all()

    pagination_class = PageNumberPagination
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('name', 'name_ar', 'keywords', 'brand__name', 'brand__name_ar',
                     'sub_category__name', 'sub_category__name_ar',
                     'sub_category__category__name', 'sub_category__category__name_ar',
                     'description',)


@api_view(['GET', ])
def auto_suggestion(request, search_pattern):
    """
    Provides auto suggestion list based on the input search pattern
    """
    if request.method == 'GET':
        search_pattern = u'%s' %search_pattern
        result = get_suggested_items(search_pattern)
        result = set_bold_suggestion(result, search_pattern)

        if len(result) == 0:
            return Response(data={"message": "suggestions not found"}, status=status.HTTP_404_NOT_FOUND)

        return Response(result)


def get_suggested_items(search_pattern):
    result = []
    required_items = 10
    search_pattern = search_pattern.lower()
    products = Product.objects.filter(
        Q(name__icontains=search_pattern) | Q(name_ar__icontains=search_pattern)
    ).filter(active=True).all()[:required_items]

    for i in products:
        if search_pattern in i.name.lower():
            result.append(i.name)
        else:
            result.append(i.name_ar)

    required_items -= len(result)
    if required_items != 0:
        subcategories = SubCategory.objects.filter(
            Q(name__icontains=search_pattern) | Q(name_ar__icontains=search_pattern)
        ).all()[:required_items]

        for i in subcategories:
            if search_pattern in i.name.lower():
                result.append(i.name)
            else:
                result.append(i.name_ar)

    required_items -= len(result)
    if required_items != 0:
        categories = Category.objects.filter(
            Q(name__icontains=search_pattern) | Q(name_ar__icontains=search_pattern)
        ).all()[:required_items]

        for i in categories:
            if search_pattern in i.name.lower():
                result.append(i.name)
            else:
                result.append(i.name_ar)

    if required_items != 0:
        brands = Brand.objects.filter(
            Q(name__icontains=search_pattern) | Q(name_ar__icontains=search_pattern)
        ).all()[:required_items]

        for i in brands:
            if search_pattern in i.name.lower():
                result.append(i.name)
            else:
                result.append(i.name_ar)

    return result


def set_bold_suggestion(input_list, search_pattern):
    for i in range(0, len(input_list)):
        element_name = input_list[i].lower()
        search_pattern = search_pattern.lower()
        element_name = element_name.replace(search_pattern, f'<b>{search_pattern}</b>')
        input_list[i] = element_name
    return input_list
