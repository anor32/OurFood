
from django import forms
from django.forms import TextInput, Select

from products.models import ParrentCategory, Category


class ParentCategoryForm(forms.ModelForm):

    class Meta:
        model = ParrentCategory
        fields = ['name', 'image']


class CategoryForm(forms.ModelForm):
    class Meta:
        fields = ('name', 'parent_category')
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
