from django.db import models
from django.db.models import ForeignKey

from users.models import NULLABLE


# Create your models here.

# здесь имеется ввиду типа вся готовая еда молочная продукция ,овощи
# максимально общие
class ParrentCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name="category_name")
    image = models.ImageField(upload_to='media/parent_categories_images/',**NULLABLE, verbose_name='parent Category Image')
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

#честно сказать я ещё не особо решил что у меня будет за проект
# наверноя я попробую делать доставку у меня большая проблема с идеями
# единственное что мне приходит в голову это проект доставки так как я могу подсмотреть у других как лучше сделать
# но это не точно
# касательно остатков с базы данных я наверное просто свою базу напишу абстрактную а потом если будет надо реальный  сайт сделать
# напишу код так чтобы просто другую базу данных подставить можно было и все
#я надеюсь вы мне подскажете если что можно ли так вообще
# в случае если подтянуть какую нибудь серьезную базу а там будут другие столбцы и не будут подходить к моей таблице
# значит подгоню под свою таблицу
# и возьму только те столбцы которые мне нужны