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
    product_name = serializers.SerializerMethodField('get_product_name')
    product_description = serializers.SerializerMethodField('get_product_description')

    def get_product_name(self, obj):
        lang = self.context.get("lang")
        if lang == 'en':
            return obj.name
        else:
            return obj.name_ar

    def get_product_description(self, obj):
        lang = self.context.get("lang")
        if lang == 'en':
            return obj.description
        else:
            return obj.description_ar

    class Meta:
        model = Product
        fields = ('id', 'brand_name', 'sub_category', 'product_name', 'price1', 'price2', 'product_description',
                  'image1', 'image2', 'image3', 'image4', 'image5', 'brand',)
