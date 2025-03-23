from django.db import models
from django.db.models import ForeignKey

from users.models import NULLABLE


# Create your models here.

# здесь имеется ввиду типа вся готовая еда молочная продукция ,овощи
# максимально общие
class ParrentCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name="category_name")

    class Meta:
        verbose_name = "ParentCategory"
        verbose_name_plural = "ParentCategories"

# а тут например родитель овощи и тут дальше идет огурцы помидоры разновидности сыры масла
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="category_name")
    parent_category = ForeignKey(ParrentCategory, on_delete=models.CASCADE, verbose_name="Parent Category", **NULLABLE)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Product_name')
    categoryID = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Category")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Price')
    quantity = models.IntegerField(null=False, default=0, verbose_name="Quantity")
    decstipriton = models.CharField(max_length=1000, verbose_name='Description', **NULLABLE)
    barcode = models.IntegerField(null=False, default=0, verbose_name="Barcode")
    img = models.ImageField(upload_to='products/images/', null=True, blank=True, verbose_name='Product Image')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        # app_label = "Products"
        # ordering = [-1]
        db_table = "goods"
        # get_latest_by ="Price"