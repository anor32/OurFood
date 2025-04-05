from django import forms

from products.models import ParrentCategory


class ParentCategoryForm(forms.ModelForm):
    class Meta:
        model = ParrentCategory
        fields = ("__all__")