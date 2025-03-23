

from django.shortcuts import render
from products.models import ParrentCategory ,Category , Product
# Create your views here.


def index(request):
    context = {
        'objects_list': ParrentCategory.objects.all()[:3],
        'ttitle': 'Моя Доставка Главная страница'
    }
    return render(request, "products/index.html",context)