from itertools import product

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView

from orders.models import Order, OrderProduct
from products.models import Product


# Create your views here.


class OrderCreate(CreateView):
    model = Order
    fields = ('products', 'order_user',)
    success_url = reverse_lazy('users:success_payment')

    def post(self, request, *args, **kwargs):
        cart = request.session['cart']
        OrderProducts = []
        for i in range(len(cart)):
            product = Product.objects.get(id=cart[i]['id'])
            ordProd =  OrderProduct.objects.create(productId=product, quantity = cart[i]['quantity'])
            OrderProducts.append(ordProd)


        order = Order.objects.create(order_user=request.user)
        order.products.set(OrderProducts)
        print("заказ создан")

        return redirect(reverse('users:success_payment'))
