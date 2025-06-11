from itertools import product

from django.urls import path

from orders.apps import OrdersConfig
from orders.views import OrderCreate, OrderList, OrderDelete, OrderSuccess

from products.views import (index_view, categories_list_view,
                            product_view, ParentCategoryCreate, ParentCategoryUpdate, ParentCategoryDelete,
                            CategoryCreate, CategoryUpdate, ProductCreate, ProductUpdate, CategoryDelete, ProductDelete,
                            ProductChoice, CartClear, SearchProduct)


app_name = OrdersConfig.name

urlpatterns = [
    path('order/',OrderCreate.as_view(),name="cart_order"),
    path('panel/',OrderList.as_view(), name="order_panel"),
    path('delete/<int:pk>/',OrderDelete.as_view(), name="order_delete"),
    path('order/success/', OrderSuccess.as_view(), name="success_payment"),
]