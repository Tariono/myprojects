from django.contrib import admin
from django.urls import path,include
from .views import *


urlpatterns = [
    path('', products_list, name='product_list_url'),
    path('product/create/', ProductCreate.as_view(), name='product_create_url'),
    path('product/<str:slug>/', ProductDetail.as_view(), name='product_detail_url'),
    path('product/<str:slug>/update/', ProductUpdate.as_view(), name='product_update_url'),
    path('product/<str:slug>/delete/', ProductDelete.as_view(), name='product_delete_url'),
]
