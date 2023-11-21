from django.contrib import admin
from django.urls import path
from intern_management_system import views

urlpatterns = [
    path('', views.homeInternPage, name='home'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser),
    path('leave_app/', views.leaveApplication),
    path('records/', views.pastRecordsPage),
]
