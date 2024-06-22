from django.shortcuts import render
from .models import Facts


def index(request):
    projects = Facts.objects.all()
    return render(request, 'facts/index.html', {"projects": projects})
