from django.shortcuts import render
from .models import Projects

# Create your views here.
def index_home(request):
    total_projects = Projects.objects.all().count()
    projects = Projects.objects.all()
    return render(request, "home.html",
    context={
        "total_projects":total_projects,
        "projects":projects
        })