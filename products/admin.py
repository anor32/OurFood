from django.contrib import admin

from products.models import Product, Category, ParrentCategory


# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk','name')
    list_filter = ('price',)
    ordering = ("pk",)



@admin.register(Category)
class categoryAdmin(admin.ModelAdmin):
    list_display = ('pk','name','parent_category')


@admin.register(ParrentCategory)
class parentCategoryAdmin(admin.ModelAdmin):
    list_display = ('pk','name')
    ordering = ('pk',)