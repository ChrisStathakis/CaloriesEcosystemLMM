from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
# Create your views here.

from .forms import LoginForm, RegisterForm


def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('homepage')
   
    return render(request, 'login.html', {'form': form})


def register_view(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        password2 = form.cleaned_data.get('password2')
        if password == password2:
            qs = User.objects.filter(username=username)
            if qs.exists():
                return render(request, 'register.html', {'error': 'Username is already taken'})
            user = User.objects.create_user(username=username, password=password)
            login(request, user)
            return redirect('account')
        
    return render(request, 'register.html', {'form': form})
       


def logout_view(request):
    logout(request)
    return redirect('login')


