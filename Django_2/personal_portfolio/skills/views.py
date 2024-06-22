from django.shortcuts import render
from .models import Skills


def index(request):
    projects = Skills.objects.all()
    return render(request, 'facts/index.html', {"projects": projects})
