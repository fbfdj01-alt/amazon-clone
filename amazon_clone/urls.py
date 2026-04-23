from django.contrib import admin
from django.urls import path
from shop.views import product_list, add_product

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', product_list, name='product_list'),
    path('add/', add_product, name='add_product'),
]
