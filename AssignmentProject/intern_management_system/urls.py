from django.contrib import admin
from django.urls import path
from intern_management_system import views

urlpatterns = [
    path('', views.index, name='home'),
]
