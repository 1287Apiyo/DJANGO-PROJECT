from django.urls import path
from django.contrib import admin
from . import views
from Ecommerce import views

urlpatterns=[
    path('product_list', views.product_list, name='product_list')
]