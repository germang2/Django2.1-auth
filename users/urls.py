from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from users import views

app_name = 'users'
urlpatterns = [
    path('login/', views.loginView, name="login"),   
    path('signin/', views.signin, name="signin"),
    path('logout/', views.logoutView, name="logout"),
]