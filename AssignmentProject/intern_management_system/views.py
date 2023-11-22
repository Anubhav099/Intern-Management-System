from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from . import models

# Create your views here.
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect("login")

def homeInternPage(request):
    if request.user.is_anonymous:
        return redirect("login")
        # retrive the logged in user data object
    x = request.user
    context = {
        'a': x.username,
        'b': x.role,
    }
    print(context)
    return render(request, 'personal_info.html', context)
        

def leaveApplication(request):
    return render(request, 'leave_app.html')

def pastRecordsPage(request):
    return render(request, 'records.html')