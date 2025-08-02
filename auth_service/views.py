# from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def register_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken')
            return redirect('register')
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request, 'User registered successfully')
        return redirect('login')
    return render(request, 'auth_service/register.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # We'll define this later
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
    return render(request, 'auth_service/login.html')

def logout_user(request):
    logout(request)
    return redirect('login')

# Create your views here.

def logout_view(request):
    logout(request)
    return redirect('login')  # or 'home' if you have a homepage

@login_required
def dashboard_view(request):
    return render(request, 'auth_service/dashboard.html')
