from django.shortcuts import render
from .models import Brand, Category, SubCategory, Product
from rest_framework import serializers, viewsets


# Create your views here.
class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SubCategorySerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(read_only=True, source='category.name')

    class Meta:
        model = SubCategory
        fields = '__all__'


class SubCategoryViewSet(viewsets.ModelViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer


class ProductSerializer(serializers.ModelSerializer):
    brand_name = serializers.CharField(read_only=True, source='brand.name')
    sub_category = SubCategorySerializer(many=False, read_only=True)

    class Meta:
        model = Product
        fields = '__all__'


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

