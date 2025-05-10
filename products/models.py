from django.db import models
from django.db.models import ForeignKey, BooleanField

from users.models import NULLABLE


# Create your models here.

# здесь имеется ввиду типа вся готовая еда молочная продукция ,овощи
# максимально общие
class ParrentCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name="category_name")
    image = models.ImageField(upload_to='media/parent_categories_images/', **NULLABLE,
                              verbose_name='parent Category Image')

    class Meta:
        verbose_name = "ParentCategory"
        verbose_name_plural = "ParentCategories"


    def __str__(self):
        return self.name



class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название подкатегории ")
    parent_category = ForeignKey(ParrentCategory, on_delete=models.CASCADE, verbose_name="Выбор Основной категории", **NULLABLE)
    has_slider = models.BooleanField(default=False,verbose_name='Создать слайдер с категорией')


    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ['name']
    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Product_name')
    categoryID = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Category")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Price')
    quantity = models.IntegerField(null=False, default=0, verbose_name="Quantity")
    description= models.CharField(max_length=1000, verbose_name='Description', **NULLABLE)
    barcode = models.IntegerField(null=False, default=0, verbose_name="Barcode")
    img = models.ImageField(upload_to='products/images/',**NULLABLE,verbose_name='Product Image',)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        # app_label = "Products"
        # ordering = [-1]
        db_table = "goods"
        # get_latest_by ="Price"


