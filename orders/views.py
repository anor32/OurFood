from itertools import product

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, TemplateView

from orders.models import Order, OrderProduct
from orders.validators import valid_date, valid_name_card, valid_number_card, valid_cvv
from products.models import Product
from utils.suply_functions import to_json


# Create your views here.


class OrderCreate(LoginRequiredMixin,CreateView):
    model = Order
    template_name = 'payment_page.html'

    fields = ('products', 'order_user',)
    success_url = reverse_lazy('orders:success_payment')

    def post(self, request, *args, **kwargs):
        if request.session['cart']:
            cart = request.session['cart']
        else:
            return HttpResponseForbidden("Доступ запрещён: корзина пуста")
        total_sum = 0
        OrderProducts = []
        for i in range(len(cart)):
            product = Product.objects.get(id=cart[i]['id'])
            total_sum += cart[i]['price']*cart[i]['quantity']
            ordProd = OrderProduct.objects.create(product=product, quantity=cart[i]['quantity'])
            OrderProducts.append(ordProd)

        order = Order.objects.create(order_user=request.user, totalSum=total_sum)
        order.products.set(OrderProducts)
        print("заказ создан")

        cart = request.session['cart']
        for cart_product in cart:
            pk = cart_product['id']
            product = get_object_or_404(Product, pk=pk)
            product.quantity -= cart_product['quantity']
            product.save()


        json = dict(request.POST)
        errors = []
        try:
            valid_name_card(json['card-name'][0])
        except ValidationError as e:
            errors.extend(e.messages)

        try:
            valid_date(json['card-expiration'][0])
        except ValidationError as e:
            errors.extend(e.messages)

        try:
            valid_number_card(json['card-number'][0])
        except ValidationError as e:
            errors.extend(e.messages)

        try:
            valid_cvv(json['card-ccv'][0])
        except ValidationError as e:
            errors.extend(e.messages)
        if errors:
            return render(request, 'payment_page.html', {'errors': errors, 'data': json})

        print('оплата прошла успешно')
        json['user'] = str(self.request.user)
        to_json('payment', json)
        request.session['cart'] = []
        return redirect(reverse('orders:success_payment'))


class OrderList(LoginRequiredMixin,ListView):
    model = Order
    template_name = 'orderPanel.html'

    def get_queryset(self):
        return Order.objects.all()


class OrderDelete(LoginRequiredMixin,DeleteView):
    model = Order
    success_url = reverse_lazy('orders:order_panel')


class OrderSuccess(LoginRequiredMixin,TemplateView):
    template_name = 'success_payment.html'
