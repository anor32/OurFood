from lib2to3.fixes.fix_input import context

from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse, get_object_or_404
from django.template.context_processors import request
from django.urls import reverse_lazy
from unicodedata import category

from products.forms import ParentCategoryForm, CategoryForm, ProductForm
from products.models import ParrentCategory, Category, Product
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView


# Create your views here.


def index_view(request):
    context = {
        'objects_list': ParrentCategory.objects.all(),
        'title': 'Моя Доставка Главная страница',
    }
    return render(request, "products/index.html", context)


def categories_list_view(request, pk):
    category_item = ParrentCategory.objects.get(pk=pk)
    categories = Category.objects.filter(parent_category=pk)
    products_list = Product.objects.filter(categoryID__in=categories)

    context = {
        "objects_list": categories,
        "title": category_item.name,
        'products_list': products_list
    }
    return render(request, 'products/categories.html', context)


class ParentCategoryUpdate(UpdateView):
    model = ParrentCategory
    template_name = 'products/create-update.html'
    success_url = reverse_lazy('products:index')
    form_class = ParentCategoryForm


# def parent_category_change_view(request, pk=None):
#     if pk:
#         category_object = get_object_or_404(ParrentCategory, pk=pk)
#     else:
#         category_object = None
#     if request.method == "POST":
#
#         form = ParentCategoryForm(request.POST, request.FILES, instance=category_object)
#         if form.is_valid():
#             parent_object = form.save()
#             parent_object.owner = request.user
#             parent_object.save()
#             return HttpResponseRedirect(reverse('products:index'))
#     context = {
#         'form': ParentCategoryForm(),
#         'object': category_object
#     }
#     return render(request, 'products/change.html', context)


class ParentCategoryCreate(CreateView):
    model = ParrentCategory
    template_name = 'products/create-update.html'
    success_url = reverse_lazy('products:index')
    form_class = ParentCategoryForm


class ParentCategoryDelete(DeleteView):
    model = ParrentCategory
    success_url = reverse_lazy('products:index')


class CategoryCreate(CreateView):
    model = Category
    template_name = 'products/create_update_category.html'
    success_url = reverse_lazy('products:index')
    form_class = CategoryForm


class CategoryUpdate(UpdateView):
    model = Category
    template_name = 'products/create_update_category.html'
    success_url = reverse_lazy('products:index')
    form_class = CategoryForm


class CategoryDelete(DeleteView):
    model = Category
    success_url = reverse_lazy('products:index')


def product_view(request):
    product_obj = Product.objects.all()

    context = {"title": "hi",
               "objects_list": product_obj,

               }
    return render(request, 'products/product_card.html')


class ProductCreate(CreateView):
    model = Product
    template_name = 'products/create_update_product.html'
    success_url = reverse_lazy('products:index')
    form_class = ProductForm


class ProductUpdate(UpdateView):
    model = Product
    template_name = 'products/create_update_product.html'
    success_url = reverse_lazy('products:index')
    form_class = ProductForm


class ProductDelete(DeleteView):
    model = Product
    success_url = reverse_lazy('products:index')
