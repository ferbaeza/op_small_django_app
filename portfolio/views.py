from wsgiref.util import request_uri
from django.shortcuts import render, get_object_or_404
from .models import Project

# Create your views here.
def index(request):
    projects = Project.objects.all()
    return render(request, "index.html", {"projects": projects})


def preview_project(request, project_id):
    project = get_object_or_404(Project, pk= project_id)
    return render(request, 'project_details.html', {'project':project})