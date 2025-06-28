from itertools import product

from django.urls import path
from django.views.decorators.cache import never_cache, cache_page

from orders.apps import OrdersConfig
from orders.views import OrderCreate, OrderList, OrderDelete, OrderSuccess

from products.views import (index_view, categories_list_view,
                             ParentCategoryCreate, ParentCategoryUpdate, ParentCategoryDelete,
                            CategoryCreate, CategoryUpdate, ProductCreate, ProductUpdate, CategoryDelete, ProductDelete,
                            ProductChoice, CartClear, SearchProduct)


app_name = OrdersConfig.name
urlpatterns = [
        path('order/',OrderCreate.as_view(),name="cart_order"),
        path('panel/',never_cache( OrderList.as_view()), name="order_panel"),
        path('delete/<int:pk>/',OrderDelete.as_view(), name="order_delete"),
        path('order/success/', OrderSuccess.as_view(), name="success_payment"),
    ]