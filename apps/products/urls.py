from django.conf.urls import url
from django.urls import path, include

from rest_framework import routers
from .views import (
    category_list, sub_category_list, slider_list,
    subcategory_product_list, category_product_list, trending_product_list,
    best_selling_product_list, ApiProductList, product_details, auto_suggestion
)

# router = routers.DefaultRouter()
# router.register(r'brands', BrandViewSet)
# router.register(r'categories', CategoryViewSet)
# router.register(r'subcategories', SubCategoryViewSet)
# router.register(r'products', ProductViewSet)

urlpatterns = [
    path('categories/<str:lang>', category_list, name="category-list"),
    path('subcategories/<str:lang>', sub_category_list, name="sub_category-list"),
    path('slider/<str:lang>', slider_list, name="slider-list"),
    path('subcategories/<int:subcategory_id>/<int:currency_id>/<str:lang>',
         subcategory_product_list, name="subcategory-product-list"),
    path('categories/<int:category_id>/<int:currency_id>/<str:lang>',
         category_product_list, name="category-product-list"),
    path('trending/<int:currency_id>/<str:lang>',
         trending_product_list, name="trending-product-list"),
    path('best-selling/<int:currency_id>/<str:lang>',
         best_selling_product_list, name="best-selling-product-list"),
    path('search/<int:currency_id>/<str:lang>/',
         ApiProductList.as_view(), name="category-product-search"),
    path('<int:product_id>/<int:currency_id>/<str:lang>/',
         product_details, name="product-details"),
    path('auto-suggestion/<str:search_pattern>/',
         auto_suggestion, name="auto-suggestion-list"),

]
