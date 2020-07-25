from django.urls import path, include
from rest_framework import routers
from .views import BrandViewSet, CategoryViewSet, SubCategoryViewSet, ProductViewSet


router = routers.DefaultRouter()
router.register(r'brands', BrandViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'subcategories', SubCategoryViewSet)
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls))
]