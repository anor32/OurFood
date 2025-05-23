from itertools import product

from django.urls import path

from orders.apps import OrdersConfig
from orders.views import OrderCreate

from products.views import (index_view, categories_list_view,
                            product_view, ParentCategoryCreate, ParentCategoryUpdate, ParentCategoryDelete,
                            CategoryCreate, CategoryUpdate, ProductCreate, ProductUpdate, CategoryDelete, ProductDelete,
                            ProductChoice, CartClear, SearchProduct)


app_name = OrdersConfig.name

urlpatterns = [
    path('order/',OrderCreate.as_view(),name ="cart_order")

]