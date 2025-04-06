from itertools import product

from django.urls import path
from products.views import index_view, products_view, categories_list_view, all_list_products_view, \
    parent_category_change_view
from products.apps import ProductsConfig

app_name = ProductsConfig.name

urlpatterns = [
    path('',index_view,name='index'),
    # path('',products_view, name = 'categories'),
    path('products/<int:pk>/categories/',categories_list_view, name = 'categories'),
    path('product/',all_list_products_view,name = 'products'),
    path('product/<int:pk>/change',parent_category_change_view,name = 'change'),
    path('product/create',parent_category_change_view,name = 'create')


]