from itertools import product

from django.urls import path

from products.models import Category, Product
from products.views import (index_view, categories_list_view,
                            product_view, ParentCategoryCreate, ParentCategoryUpdate, ParentCategoryDelete,
                            CategoryCreate, CategoryUpdate, ProductCreate, ProductUpdate, CategoryDelete, ProductDelete,
                            ProductChoice)
from products.apps import ProductsConfig

app_name = ProductsConfig.name

urlpatterns = [
    path('',index_view,name='index'),
    # path('',products_view, name = 'categories'),
    path('products/<int:pk>/categories/',categories_list_view, name = 'categories'),
    path('products/categories/product',product_view,name = 'product_card'),

    #parentcategory crud
    path('product/<int:pk>/change',ParentCategoryUpdate.as_view(),name = 'change'),
    path('products/delete/<int:pk>/', ParentCategoryDelete.as_view(), name='delete_parent_category'),
    path('products/create',ParentCategoryCreate.as_view(),name = 'create'),
    #category crud
    path('products/create/category',CategoryCreate.as_view(),name = 'category_create'),
    path('products/update/<int:pk>/category',CategoryUpdate.as_view(),name = 'category_update'),
    path('products/delete/<int:pk>/category',CategoryDelete.as_view(),name = 'category_delete'),

    #product crud
    path("products/create/product" ,ProductCreate.as_view(),name= 'product_create'),
    path("products/update/<int:pk>/product",ProductUpdate.as_view(),name= 'product_update'),
    path('product/<int:pk>/delete/product', ProductDelete.as_view(), name='product_delete'),

    #product choice
    path('product/<int:pk>/choice/product', ProductChoice.as_view(), name='product_choice')
]