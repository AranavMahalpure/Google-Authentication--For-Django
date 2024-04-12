from django.shortcuts import render
from django.contrib.auth import logout as auth_logout

def home(request):
    return render(request, 'home.html')

def logout_view(request):
    auth_logout(request)
    return render(request, 'logout.html')