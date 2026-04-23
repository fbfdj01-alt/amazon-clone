from django.contrib import admin
from django.urls import path
from shop.views import add_product

urlpatterns = [
    path('admin/', admin.site.url),
    path('add/', add_product, name='add_product'), # هذا رابط صفحة الإضافة
]
