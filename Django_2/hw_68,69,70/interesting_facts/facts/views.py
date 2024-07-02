from django.shortcuts import render, get_object_or_404, redirect
from .models import Facts
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .forms import FactsForm


def home(request):
    return render(request, 'facts/home.html')


def index(request):
    projects = Facts.objects.all()
    return render(request, 'facts/index.html', {"projects": projects})


def detail(request, project_id):
    project = get_object_or_404(Facts, pk=project_id)
    return render(request, 'facts/details.html', {'project': project})


def signup(request):
    if request.method == "GET":
        return render(request, 'facts/signup.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('index')
            except IntegrityError:
                return render(request, 'facts/signup.html',
                              {'form': UserCreationForm(),
                               'error': "Такое имя пользователя уже существует. Задайте другое"})
        else:
            return render(request, 'facts/signup.html',
                          {'form': UserCreationForm(),
                           'error': "Пароли не совпадают"})


def logouting(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')


def logining(request):
    if request.method == "GET":
        return render(request, 'facts/login.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'facts/login.html',
                          {'form': AuthenticationForm(),
                           'error': "Неверные данные"})
        else:
            login(request, user)
            return redirect('index')


def add_fact(request):
    if request.method == "GET":
        return render(request, 'facts/add_fact.html', {'form': FactsForm()})
    else:
        try:
            form = FactsForm(request.POST)
            new_fact = form.save(commit=True)
            new_fact.user = request.user
            new_fact.save()
            return redirect('index')
        except ValueError:
            return render(request, 'facts/add_fact.html', {
                "form": FactsForm(),
                "error": "Переданы неверные данные. Попробуйте еще раз"})
