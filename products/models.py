from django.db import models
from django.db.models import ForeignKey

from users.models import NULLABLE


# Create your models here.

# здесь имеется ввиду типа вся готовая еда молочная продукция ,овощи
# максимально общие
class ParentCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name="category_name")
    image = models.ImageField(upload_to='media/parent_categories_images/', **NULLABLE,
                              verbose_name='parent Category Image')
    priority = models.IntegerField(default=0,verbose_name='priority')

    class Meta:
        verbose_name = "ParentCategory"
        verbose_name_plural = "ParentCategories"
        ordering = ['-priority','id']

    def __str__(self):
        return self.name



class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название подкатегории ")
    parent_category = ForeignKey(ParentCategory, on_delete=models.CASCADE, verbose_name="Выбор Основной категории")
    has_slider = models.BooleanField(default=False,verbose_name='Создать слайдер с категорией')
    priority = models.IntegerField(default=0,verbose_name='priority')
    products = models.ManyToManyField('products.Product' ,related_name="products_lists",verbose_name="add product")

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ['-priority','name']
    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Product_name')

    categoryID = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Category",related_name='category')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Price')
    quantity = models.IntegerField(null=False, default=0, verbose_name="Quantity")
    description= models.CharField(max_length=1000, verbose_name='Description', **NULLABLE)
    barcode = models.IntegerField(null=False, default=0, verbose_name="Barcode")
    img = models.ImageField(upload_to='products/images/',**NULLABLE,verbose_name='Product Image',)
    priority = models.IntegerField(default=0,verbose_name='priority')
    discount = models.IntegerField(default=0,verbose_name="Скидка")
    original_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='original price',default=0)
    composition = models.CharField(max_length=1000, verbose_name='Cостав', **NULLABLE)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

        ordering = ['-priority','id']
        db_table = "goods"




