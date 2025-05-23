from django.template.defaultfilters import default
from django.utils import timezone
from tkinter.constants import CASCADE

from django.db import models

from products.models import Product
from users.models import NULLABLE

from users.models import User
# Create your models here.

class Order(models.Model):
    statuses = (
        ("assembling", "Assembling"),
        ("delivery", "Delivery"),
        ("completed", "Completed"),
    )
    order_user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="Заказчик")
    products = models.ManyToManyField(Product, related_name="ordered_products")
    datetime = models.DateTimeField(verbose_name="дата заказа", default=timezone.now)
    status = models.CharField(verbose_name="статус заказа", default="Assembling", choices=statuses, max_length=50)
    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"
        ordering = ['id']

    def __str__(self):
        return self.name
