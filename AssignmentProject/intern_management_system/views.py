from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def loginPage(request):
    return render(request, 'login.html')

def homeInternPage(request):
    return render(request, 'personal_info.html')

def leaveApplication(request):
    return render(request, 'leave_app.html')

def pastRecordsPage(request):
    return render(request, 'records.html')