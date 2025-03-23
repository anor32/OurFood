from django.urls import path
from products.views import index
from products.apps import ProductsConfig

app_name = ProductsConfig.name

urlpatterns = [
    path('',index,name='index'),
]