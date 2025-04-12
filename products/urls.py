from itertools import product

from django.urls import path
from products.views import (index_view, categories_list_view,
                            product_view, ParentCategoryCreate, ParentCategoryUpdate, ParentCategoryDelete,)
from products.apps import ProductsConfig

app_name = ProductsConfig.name

urlpatterns = [
    path('',index_view,name='index'),
    # path('',products_view, name = 'categories'),
    path('products/<int:pk>/categories/',categories_list_view, name = 'categories'),
    path('products/categories/product',product_view,name = 'product_card'),
    path('product/<int:pk>/change',ParentCategoryUpdate.as_view(),name = 'change'),
    path('product/delete/<int:pk>/', ParentCategoryDelete.as_view(), name='delete_category'),
    path('product/create',ParentCategoryCreate.as_view(),name = 'create'),

]