from django.shortcuts import render, redirect
from users.forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
# Create your views here.


def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username=username, password=password)
        login(request, user)
        messages.success(request, 'Başarı ile giriş yaptınız')
        return redirect('index')
    context = {
        'form': form
    }
    return render(request, 'users/login.html', context)


def register_view(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        messages.success(request, 'Başarı ile kayıt oldunuz.')
        return redirect('index')
    else:
        return render(request, 'users/register.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.success(request, 'Başarı ile çıkış yaptınız.')
    return redirect('index')