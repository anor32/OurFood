from tkinter.constants import CASCADE

from django.db import models

from products.models import Product
from users.models import NULLABLE

from users.models import User
# Create your models here.

class Order(models.Model):
    order_user = models.ForeignKey(User, on_delete=models.SET_DEFAULT, verbose_name="Заказчик")
    products = models.ManyToManyField(Product, related_name="ordered_products")


    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"
        ordering = ['id']

    def __str__(self):
        return self.name
