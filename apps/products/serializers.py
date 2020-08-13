from rest_framework import serializers

from apps.products.models import Category, SubCategory, Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class SubCategorySerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(read_only=True, source='category.name')

    class Meta:
        model = SubCategory
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    brand_name = serializers.CharField(read_only=True, source='brand.name')
    sub_category = SubCategorySerializer(many=False, read_only=True)

    class Meta:
        model = Product
        fields = '__all__'

