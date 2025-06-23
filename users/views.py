

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse, redirect, get_object_or_404

from django.contrib.auth.views import LoginView, PasswordChangeView, LogoutView
from django.views.generic import CreateView, UpdateView, ListView, View, TemplateView
from django.urls import reverse_lazy

from products.models import Product
from users.models import User
from users.forms import UserRegisterForm, UserLoginForm, UserUpdateForm, UserPasswordChangeForm,  UserForm
from users.servises import send_new_password
import json



class UserRegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('products:index')
    template_name = 'users/user_register.html'
    extra_context = {
        'title': 'Создать аккаунт',
    }

    def form_valid(self, form):
        self.object = form.save()
        return super().form_valid(form)


class UserLoginView(LoginView):
    template_name = 'users/user_login.html'
    success_url = reverse_lazy('users:user_profile')
    form_class = UserLoginForm
    extra_context = {
        'title': 'Вход В аккаунт',
    }


class UserProfileView(UpdateView):
    model = User
    form_class = UserForm
    template_name = 'users/user_profile_read_only.html'
    extra_context = {
        'title': f'Ваш Профиль '
    }

    def get_object(self, queryset=None):
        return self.request.user


class UserUpdateView(UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'users/user_update.html'
    success_url = reverse_lazy('users:user_profile')
    extra_context = {
        'title': 'Обновить профиль',
    }

    def post(self, request, *args, **kwargs):
        print("Form submitted")  # Add this line
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        if form.is_valid():
            print('valid')

            return super().form_valid(form)
        else:
            print(form.errors)
            return self.form_invalid(form)

    def get_object(self, queryset=None):
        return self.request.user


class UserLogoutView(LoginRequiredMixin,LogoutView):
        template_name = 'users/user_logout.html'
        extra_context = {
            'title': 'Выход из аккаунта',
        }


class UserChangePasswordView(PasswordChangeView):
    from_class = UserPasswordChangeForm
    template_name = 'users/user_change_password.html'
    success_url = reverse_lazy('users:user_profile')
    extra_context = {
        'title': 'Измениние пароля',
    }







