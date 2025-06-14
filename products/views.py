from itertools import product
from lib2to3.fixes.fix_input import context

from PIL.ImageShow import Viewer
from django.contrib.auth.mixins import PermissionRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse, get_object_or_404, redirect
from django.template.context_processors import request
from django.urls import reverse_lazy
from unicodedata import category
from django.db.models import Q
from products.forms import ParentCategoryForm, CategoryForm, ProductForm
from products.models import ParentCategory, Category, Product
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, View

from users.mixins import StaffRequiredMixin


# Create your views here.


def index_view(request):
    context = {
        'objects_list': ParentCategory.objects.all(),
        'products_list': Product.objects.all(),
        'title': 'Моя Доставка Главная страница',
    }
    return render(request, "products/index.html", context)


def categories_list_view(request, pk):
    category_item = ParentCategory.objects.get(pk=pk)
    categories = Category.objects.filter(parent_category=pk)
    products_list = Product.objects.filter(categoryID__in=categories)

    context = {
        "objects_list": categories,
        "title": category_item.name,
        'products_list': products_list
    }
    return render(request, 'products/categories.html', context)


class ParentCategoryUpdate(StaffRequiredMixin, UpdateView):
    model = ParentCategory
    template_name = 'products/create-update.html'
    success_url = reverse_lazy('products:index')
    permission_required = ''
    form_class = ParentCategoryForm




class ParentCategoryCreate(StaffRequiredMixin,CreateView):
    model = ParentCategory
    template_name = 'products/create-update.html'
    success_url = reverse_lazy('products:index')
    form_class = ParentCategoryForm


class ParentCategoryDelete(StaffRequiredMixin,DeleteView):
    model = ParentCategory
    success_url = reverse_lazy('products:index')


class CategoryCreate(StaffRequiredMixin,CreateView):
    model = Category
    template_name = 'products/create_update_category.html'
    success_url = reverse_lazy('products:index')
    form_class = CategoryForm


class CategoryUpdate(StaffRequiredMixin,UpdateView):
    model = Category
    template_name = 'products/create_update_category.html'
    success_url = reverse_lazy('products:index')
    form_class = CategoryForm


class CategoryDelete(StaffRequiredMixin,DeleteView):
    model = Category
    success_url = reverse_lazy('products:index')


def product_view(request):
    product_obj = Product.objects.all()

    context = {"title": "hi",
               "objects_list": product_obj,

               }
    return render(request, 'products/product_card.html')


class ProductDetail(DetailView):
    model = Product
    template_name = 'products/product_detail.html'



class ProductCreate(StaffRequiredMixin,CreateView):
    model = Product
    template_name = 'products/create_update_product.html'
    success_url = reverse_lazy('products:index')
    form_class = ProductForm

    def form_valid(self, form):
        response = super().form_valid(form)
        category = Category.objects.get(pk=28)
        if form.cleaned_data['discount'] > 0:
            category.products.add(self.object)
        else:
            category.products.remove(self.object)
        return response

       

class ProductUpdate(StaffRequiredMixin,UpdateView):
    model = Product
    template_name = 'products/create_update_product.html'
    success_url = reverse_lazy('products:index')
    form_class = ProductForm


    def post(self, request, *args, **kwargs):
        form = self.get_form()
        category = Category.objects.get(pk=28)
        product = self.get_object()
        if form.is_valid():

            if form.cleaned_data['discount'] > 0:
                print('here')
                category.products.add(product)

            else:
                 category.products.remove(product)


        return super().post(request, *args, **kwargs)



class ProductDelete(StaffRequiredMixin,DeleteView):
    model = Product
    success_url = reverse_lazy('products:index')


class ProductChoice(View):
    model = Product

    def post(self, request, pk):
        pk = self.kwargs['pk']

        product = get_object_or_404(Product, pk=pk)
        createdProduct = {
            'id': product.id,
            'name': product.name,
            'price': int(product.price),
            'quantity': 1,
            'img': str(product.img),
            'original_price':int(product.original_price)
        }
        price = createdProduct['price']
        if "cart" not in request.session:
            cart = []

        else:
            cart = request.session['cart']

        # if cart == [] :
        #     print('here')
        #     cart.append(createdProduct)

        for item in cart:
            print(item['quantity'],product.quantity)
            if createdProduct['id'] == item['id'] and item['quantity'] <= product.quantity-1 :
                item['quantity'] += 1
                item['price'] = price *  item['quantity']
                break

        for prod in cart:
            if prod['id'] == createdProduct['id']:
                break
        else:
            cart.append(createdProduct)
        request.session['cart'] = cart

        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

class ProductRemove(View):
    model = Product

    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)

        cart = request.session['cart']
        for cart_product in cart:
            price = cart_product['price']
            if cart_product['id'] == product.id:
                if cart_product['quantity'] == 1:
                    cart.remove(cart_product)

                else:

                    cart_product['quantity'] -=1
                    cart_product['price'] =  price - round(cart_product['price']/(cart_product['quantity']+1))


        request.session['cart'] = cart


        if product.id in cart:
            print(product)

        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
class CartClear(View):
    def post(self, request):
        if "cart" in request.session:
            request.session['cart'] = []
        return redirect(reverse('products:index'))


class SearchProduct(ListView):
    model = Product
    template_name = 'products/products_results.html'
    extra_context = {
        'title': 'Результаты поискового запроса'
    }

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Product.objects.filter(
             Q(name__icontains=query)
        )

        return object_list


