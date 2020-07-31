"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import index
from django.conf.urls.static import static
from django.conf import settings

admin.site.site_header = 'My Store'
admin.site.site_title = 'My Store'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('checkserver/', index, name='index'),
    path('auth/', include('apps.authapp.urls')),
    path('products/', include('apps.products.urls')),
    path('orders/', include('apps.orders.urls')),
]

# to enable viewing images in media directory
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)