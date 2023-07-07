from django.shortcuts import render, redirect, Http404
from .form import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, logout

def login_view(request):
    form = LoginForm(request.POST or None)

    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('home')

    return  render(request, 'accounts/form.html', {'form': form})

def register_view(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        newUser = authenticate(username=user.username, password=password)
        login(request, newUser)
        return redirect('home')
    return render(request, 'accounts/register.html', {'form': form})

def logout_view(request):
    if not request.user.is_authenticated:
        return Http404
    logout(request)
    return redirect('home')
