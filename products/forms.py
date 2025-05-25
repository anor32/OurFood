from django import forms
from django.forms import TextInput, Select, NumberInput

from products.models import ParentCategory, Category, Product


class ParentCategoryForm(forms.ModelForm):
    class Meta:
        model = ParentCategory
        fields = ['name', 'image', 'priority']


class CategoryForm(forms.ModelForm):
    class Meta:
        fields = ('name', 'parent_category', "has_slider", 'priority','products')
        model = Category

        widgets = {
            "name": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Название подкатегории"
            }),
            "parent_category": Select(attrs={
                "class": "form-control",
                "placeholder": "Выбор категории"
            }),
            "priority": NumberInput(attrs={
                "class": "form-control",
                "placeholder": "Выбор Приоритета вывода"
            }),
        }


class ProductForm(forms.ModelForm):
    class Meta:
        exclude = ('barcode',)
        model = Product

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'categoryID': forms.Select(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'discount':  forms.NumberInput(attrs={'class': 'form-control'}),
            'img': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            "priority": NumberInput(attrs={"class": "form-control","placeholder": "Выбор Приоритета вывода"
            }),
        }

    def clean(self):


        cleaned_price = self.cleaned_data['price']
        cleaned_discount = self.cleaned_data['discount']

        if cleaned_discount:

            self.cleaned_data['price'] = int(cleaned_price - cleaned_price*cleaned_discount/100)


        return self.cleaned_data

