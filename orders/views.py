from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import CreateView

from orders.models import Order


# Create your views here.



class OrderCreate(CreateView):
    model = Order

    def post(self, request, *args, **kwargs):
        Order.objects.create(
            products = request.session['cart'],
            order_user = request.user


        )


        return redirect(reverse('products:success_payment'))

