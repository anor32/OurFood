from django import forms

from products.models import ParrentCategory, Category


class ParentCategoryForm(forms.ModelForm):
    # name = forms.CharField(widget=forms.TextInput)
    # image = forms.ImageField(widget=forms.FileInput)

    class Meta:
        model = ParrentCategory
        fields = ['name', 'image']


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)