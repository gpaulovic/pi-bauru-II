from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib import messages


def home(request):
    return render(request, "inicio.html")


def login_page():
    return render("login.html")


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home-ecopontos')
        else:
            error_message = "Usuário ou senha inválidos."
            messages.error(request, error_message)
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')


def user_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('user_login')
        else:
            messages.error(request, form.errors)
            return render(request, 'signup.html')


def page_register(request):
    return render(request, "signup.html")


def logout_view(request):
    logout(request)
    return redirect(home)
