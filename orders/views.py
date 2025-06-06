from itertools import product


from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView

from orders.models import Order, OrderProduct
from products.models import Product
from utils.suply_functions import to_json


# Create your views here.


class OrderCreate(CreateView):
    model = Order
    template_name = 'payment_page.html'

    fields = ('products', 'order_user',)
    success_url = reverse_lazy('users:success_payment')

    def post(self, request, *args, **kwargs):
        if request.session['cart']:
            cart = request.session['cart']
        else:
            return HttpResponseForbidden("Доступ запрещён: корзина пуста")
        total_sum = 0
        OrderProducts = []
        for i in range(len(cart)):
            product = Product.objects.get(id=cart[i]['id'])
            total_sum += cart[i]['price']
            ordProd =  OrderProduct.objects.create(product=product, quantity = cart[i]['quantity'])
            OrderProducts.append(ordProd)


        order = Order.objects.create(order_user=request.user,totalSum=total_sum)
        order.products.set(OrderProducts)
        print("заказ создан")

        cart = request.session['cart']
        for cart_product in cart:
            pk = cart_product['id']
            product = get_object_or_404(Product, pk=pk)
            product.quantity -= cart_product['quantity']
            product.save()
        request.session['cart'] = []
        json = dict(request.POST)
        print('оплата прошла успешно')
        json['user'] = str(self.request.user)
        to_json('payment', json)
        return redirect(reverse('users:success_payment'))


class OrderList(ListView):
    model = Order
    template_name = 'orderPanel.html'

    def get_queryset(self):
        return Order.objects.all()


class OrderDelete(DeleteView):
    model = Order
    success_url = reverse_lazy('orders:order_panel')