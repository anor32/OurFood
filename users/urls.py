from django.urls import path

from users.apps import UsersConfig

from users.views import ( UserRegisterView, UserLoginView,
                         UserProfileView, UserLogoutView, UserUpdateView, UserChangePasswordView,
                          )
app_name = UsersConfig.name

urlpatterns = [
    path("register/", UserRegisterView.as_view(), name="user_register"),
    path("user_login/", UserLoginView.as_view(), name="user_login"),
    path("profile/", UserProfileView.as_view()  , name="user_profile"),
    path('logout/', UserLogoutView.as_view(), name='user_logout', ),
    path('update/', UserUpdateView.as_view(), name= 'user_update',),
    path("change_password/",UserChangePasswordView.as_view(),name='user_change_password'),






]
