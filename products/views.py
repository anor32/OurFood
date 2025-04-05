

from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse, get_object_or_404
from django.template.context_processors import request

from products.forms import ParentCategoryForm
from products.models import ParrentCategory ,Category , Product
# Create your views here.


def index_view(request):
    context = {
        'objects_list': ParrentCategory.objects.all(),
        'ttitle': 'Моя Доставка Главная страница'
    }
    return render(request, "products/index.html",context)


def categories_list_view(request):
    context = {
        "objects_list" : Category.objects.all(),
        "title": "Все основные Категории"
    }
    return render (request, 'products/categories',context)
def category_products_view(request,pk):
    category_item = Category.objects.get(pk = pk)
    context = {
        "objects_list": Product.filter(category_id = pk),
        "title": f"Все из категории {category_item.name}",
        "category_pk":category_item.pk,
    }
    return render(request,'products/product.html',context)
def all_list_products_view(request):
    context = {
        "objects_list": Category.objects.all(),
        "title": "Все Товары Категории"
    }
    return render(request,'products/product.html',context)

def parent_category_change_view(request,pk=None):
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
    context ={
        'form': ParentCategoryForm(),
        'object':category_object
              }
    return render(request, 'products/change.html', context)
