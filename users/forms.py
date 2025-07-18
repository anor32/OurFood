from cProfile import label

from  django import forms
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm, AuthenticationForm
from django.forms import SelectDateWidget
from django.contrib.admin.widgets import AdminDateWidget
from users.models import User
from users.validators import validate_password
from  django.core.exceptions import ValidationError
from  django.contrib.auth import password_validation
class StyleFromMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class UserRegisterForm(StyleFromMixin,UserCreationForm):
    class Meta:
        model = User
        fields = ('email',)

    def clean_password2(self):
        cleaned_data = self.cleaned_data
        validate_password(cleaned_data['password1'])
        if cleaned_data['password1'] != cleaned_data['password2']:
            print("Пароли не совпадают!!!")
            raise forms.ValidationError("Пароли не совпадают")
        return cleaned_data['password2']


class UserLoginForm(StyleFromMixin,AuthenticationForm):
    pass

class UserForm(StyleFromMixin,forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'phone')

widgets = {
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'})
}

class DateInput(forms.DateInput):
    input_type = 'date'

class UserUpdateForm(StyleFromMixin, forms.ModelForm ,forms.Form):

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'phone','date_birth','address')
    widgets = {
        'email': forms.TextInput(attrs={'class': 'form-control'}),
        'first_name': forms.TextInput(attrs={'class': 'form-control'}),
        'address': forms.TextInput(attrs={'class': 'form-control', 'id': 'address'}),
        'phone': forms.TextInput(attrs={'class': 'form-control'}),
        'date_birth': forms.DateInput(attrs={'type':'date'})
    }


class UserPasswordChangeForm(StyleFromMixin,PasswordChangeForm):
   def clean_new_password2(self):
       password1 = self.cleaned_data.get('new_password1')
       password2 = self.cleaned_data.get('new_password2')
       validate_password(password1)
       if password1 and password2 and password1 != password2:
           raise ValidationError(
               self.error_messages['password_mismatch'],
               code='password_mismatch',
           )
       password_validation.validate_password(password2,self.user)
       return password2


