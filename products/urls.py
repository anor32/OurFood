from itertools import product

from django.urls import path
from products.views import (index_view,  categories_list_view,
                            parent_category_change_view, product_view)
from products.apps import ProductsConfig

app_name = ProductsConfig.name

urlpatterns = [
    path('',index_view,name='index'),
    # path('',products_view, name = 'categories'),
    path('products/<int:pk>/categories/',categories_list_view, name = 'categories'),
    path('products/categories/product',product_view,name = 'product_card'),
    path('product/<int:pk>/change',parent_category_change_view,name = 'change'),
    path('product/create',parent_category_change_view,name = 'create')


]