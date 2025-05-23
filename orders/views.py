from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView

from orders.models import Order
from products.models import Product


# Create your views here.



class OrderCreate(CreateView):
    model = Order
    fields = ('products','order_user',)
    success_url = reverse_lazy('users:success_payment')




    def post(self, request, *args, **kwargs):

        ids = [ request.session['cart'][i]['id'] for i in range(len(request.session['cart']))]


        order = Order.objects.create(order_user=request.user)
        order.products.set(Product.objects.filter(id__in=ids)
          )
        print("заказ создан")


        return redirect(reverse('users:success_payment'))

