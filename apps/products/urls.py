from django.conf.urls import url
from django.urls import path, include

from rest_framework import routers
from .views import category_list, sub_category_list

# router = routers.DefaultRouter()
# router.register(r'brands', BrandViewSet)
# router.register(r'categories', CategoryViewSet)
# router.register(r'subcategories', SubCategoryViewSet)
# router.register(r'products', ProductViewSet)

urlpatterns = [
    path('categories/<str:lang>', category_list, name="category-list"),
    path('subcategories/<str:lang>', sub_category_list, name="sub_category-list"),
]
