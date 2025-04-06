from lib2to3.fixes.fix_input import context

from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse, get_object_or_404
from django.template.context_processors import request

from products.forms import ParentCategoryForm
from products.models import ParrentCategory, Category, Product


# Create your views here.


def index_view(request):
    context = {
        'objects_list': ParrentCategory.objects.all(),
        'title': 'Моя Доставка Главная страница'
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


def parent_category_change_view(request, pk=None):
    if pk:
        category_object = get_object_or_404(ParrentCategory, pk=pk)
    else:
        category_object = None
    if request.method == "POST":

        form = ParentCategoryForm(request.POST, request.FILES, instance=category_object)
        if form.is_valid():
            parent_object = form.save()
            parent_object.owner = request.user
            parent_object.save()
            return HttpResponseRedirect(reverse('products:index'))
    context = {
        'form': ParentCategoryForm(),
        'object': category_object
    }
    return render(request, 'products/change.html', context)


def product_view(request):
    product_obj = Product.objects.all()
    context = {"title": "hi",
               "objects_list": product_obj
               }
    return render(request, 'products/product_card.html')
