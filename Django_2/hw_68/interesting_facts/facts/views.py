from django.shortcuts import render, get_object_or_404
from .models import Facts


def index(request):
    projects = Facts.objects.all()
    return render(request, 'facts/index.html', {"projects": projects})


def detail(request, project_id):
    project = get_object_or_404(Facts, pk=project_id)
    return render(request, 'facts/details.html', {'project': project})
