
from django import forms
from django.forms import TextInput, Select

from products.models import ParrentCategory, Category, Product


class ParentCategoryForm(forms.ModelForm):

    class Meta:
        model = ParrentCategory
        fields = ['name', 'image']


class CategoryForm(forms.ModelForm):
    class Meta:
        fields = ('name', 'parent_category',"has_slider")
        model = Category

        widgets = {
            "name": TextInput(attrs={
                "class": "form-control",
                "placeholder":"Название подкатегории"
            }),
            "parent_category": Select(attrs={
                "class": "form-control",
                "placeholder": "Выбор категории"
            }),

        }


class ProductForm(forms.ModelForm):
    class Meta:
        fields = "__all__"
        model = Product
        exclude =('barcode',)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'categoryID': forms.Select(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),

            'img': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }