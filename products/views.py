from lib2to3.fixes.fix_input import context

from django.shortcuts import render
from django.template.context_processors import request

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
def category_products_view(requests,pk):
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
# пока что так написал позже как больше пониманияя появится я перепишу сейчас в основном пишу с  урока
# конкретно под свой вариант
# пока что я не особо понимаю как у меня будет структура в целом выглядть где куда я что нажимать буду и какие шаблоны нужны будут
# дальше понятнее будет