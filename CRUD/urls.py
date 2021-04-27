from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    
    path('update/' ,views.update,name="update"),
    path('delete_item/<str:pk>/' ,views.delete_item,name="delete_item"),
    path('update_item/<str:pk>/' ,views.update_item,name="update_item"),
    path('registerPage/' ,views.registerPage,name="registerPage"),
    path('loginPage/' ,views.loginPage,name="loginPage"),
    path('logoutPage/' ,views.logoutPage,name="logoutPage"),
    
]