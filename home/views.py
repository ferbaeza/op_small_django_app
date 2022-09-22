from http.client import HTTPResponse
from django.shortcuts import render
from .models import Projects, get_app_installed
from django.http import HttpResponse

# Create your views here.
def index_home(request):
    apps = get_app_installed()
    total_projects = Projects.objects.all().count()
    projects = Projects.objects.all()
    return render(request, "appGrid.html",
    context={
        "total_projects":total_projects,
        "projects":projects,
        "apps":apps
        })

def detail_project(request, id):
    if id:
        project = Projects.objects.filter(id_project=id)
        return render(request, "detail.html",{"project":project})

        # return HttpResponse(f"Yeahhh -----------{id}-----------{project} ")

    return HttpResponse(f"No se ha encontrado app con ese {id} ")