from django.conf.urls import url
from django.urls import path, include

from rest_framework import routers
from .views import category_list, sub_category_list, slider_product_list, subcategory_product_list, \
    category_product_list

# router = routers.DefaultRouter()
# router.register(r'brands', BrandViewSet)
# router.register(r'categories', CategoryViewSet)
# router.register(r'subcategories', SubCategoryViewSet)
# router.register(r'products', ProductViewSet)

urlpatterns = [
    path('categories/<str:lang>', category_list, name="category-list"),
    path('subcategories/<str:lang>', sub_category_list, name="sub_category-list"),
    path('slider/<str:lang>', slider_product_list, name="slider-list"),
    path('subcategories/<int:subcategory_id>/<str:lang>',
         subcategory_product_list, name="subcategory-product-list"),
    path('categories/<int:category_id>/<str:lang>',
         category_product_list, name="category-product-list"),

]
