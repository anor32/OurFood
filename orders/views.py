from itertools import product


from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView

from orders.models import Order, OrderProduct
from products.models import Product


# Create your views here.


class OrderCreate(CreateView):
    model = Order
    fields = ('products', 'order_user',)
    success_url = reverse_lazy('users:success_payment')

    def post(self, request, *args, **kwargs):
        cart = request.session['cart']
        total_sum = 0
        OrderProducts = []
        for i in range(len(cart)):
            product = Product.objects.get(id=cart[i]['id'])
            total_sum += cart[i]['price']
            ordProd =  OrderProduct.objects.create(product=product, quantity = cart[i]['quantity'])
            OrderProducts.append(ordProd)
        print(total_sum)

        order = Order.objects.create(order_user=request.user,totalSum=total_sum)
        order.products.set(OrderProducts)
        print("заказ создан")

        return redirect(reverse('users:success_payment'))


class OrderList(ListView):
    model = Order
    template_name = 'orderPanel.html'

    def get_queryset(self):
        return Order.objects.all()


class OrderDelete(DeleteView):
    model = Order
    success_url = reverse_lazy('orders:order_panel')