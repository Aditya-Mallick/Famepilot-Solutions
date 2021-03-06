from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('logout', views.logoutPage, name='logout'),
    path('register', views.registerPage, name='register'),
    path('login', views.loginPage, name='login'),
]
