from itertools import product

from django.urls import path
from django.views.decorators.cache import cache_page, never_cache
from products.models import Category, Product
from products.views import (index_view, categories_list_view,
                             ParentCategoryCreate, ParentCategoryUpdate, ParentCategoryDelete,
                            CategoryCreate, CategoryUpdate, ProductCreate, ProductUpdate, CategoryDelete, ProductDelete,
                            ProductChoice, CartClear, SearchProduct, ProductRemove, ProductDetail)
from products.apps import ProductsConfig
app_name = ProductsConfig.name

urlpatterns = [
        path('',index_view,name='index'),
        # path('',products_view, name = 'categories'),
        path('products/<int:pk>/categories/',categories_list_view, name = 'categories'),


        #parentcategory crud
        path('product/<int:pk>/change',never_cache(ParentCategoryUpdate.as_view()),name = 'change'),
        path('products/delete/<int:pk>/', ParentCategoryDelete.as_view(), name='delete_parent_category'),
        path('products/create',ParentCategoryCreate.as_view(),name = 'create'),
        #category crud
        path('products/create/category',never_cache(CategoryCreate.as_view()),name = 'category_create'),
        path('products/update/<int:pk>/category',CategoryUpdate.as_view(),name = 'category_update'),
        path('products/delete/<int:pk>/category',CategoryDelete.as_view(),name = 'category_delete'),

        #product crud
        path("products/create/product" ,never_cache(ProductCreate.as_view()),name= 'product_create'),
        path("products/<int:pk>/update/product",ProductUpdate.as_view(),name='product_update'),
        path('product/<int:pk>/delete/product', ProductDelete.as_view(), name='product_delete'),
        path('product/<int:pk>/detail/product', cache_page(30)(ProductDetail.as_view()), name='product_detail'),

        #cart choice
        path('product/<int:pk>/choice/product', never_cache(ProductChoice.as_view()), name='product_choice'),
        path('product/clear/',CartClear.as_view(),name='cart_clear'),
        path('product/<int:pk>/remove/product',ProductRemove.as_view(),name='product_remove'),

        #search
        path('products/search/results',SearchProduct.as_view(),name='search')

]