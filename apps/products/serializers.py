from rest_framework import serializers

from apps.currencies.models import Currency
from apps.products.models import Category, SubCategory, Product, Slider


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
    price1 = serializers.SerializerMethodField('get_price1')
    price2 = serializers.SerializerMethodField('get_price2')

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

    def get_price1(self, obj):
        currency_id = self.context.get("curr")
        currency = Currency.objects.get(pk=currency_id)
        return obj.price1 * currency.rate

    def get_price2(self, obj):
        currency_id = self.context.get("curr")
        currency = Currency.objects.get(pk=currency_id)
        return obj.price2 * currency.rate

    class Meta:
        model = Product
        fields = ('id', 'brand_name', 'sub_category', 'product_name', 'price1', 'price2', 'delivery_days',
                  'product_description', 'image1', 'image2', 'image3', 'image4', 'image5', 'brand',)


class SliderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Slider
        fields = ('name', 'image', 'link', )

