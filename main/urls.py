from django.contrib import admin
from django.urls import path, include
from . import views
from django.views.generic.base import TemplateView

from django.contrib.auth import views as auth_view

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register_user, name="register"),
    path('login/', auth_view.LoginView.as_view(template_name='main/login.html'), name='login'),
    path('logout/', auth_view.LogoutView.as_view(), name='logout'),
    path('login_success/', views.login_success, name='login_success')
]
