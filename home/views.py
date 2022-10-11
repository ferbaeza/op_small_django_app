from http.client import HTTPResponse
from pprint import pprint
from django.shortcuts import render, redirect
from .models import Projects, get_app_installed
from django.http import HttpResponse

# Create your views here.
def index_home(request):
    if request.user.is_authenticated:
        username= request.user
        apps = get_app_installed()
        app_index=Projects.objects.all().delete()
        total_apps = Projects.objects.all().count()
        if total_apps == 0:
            for app in apps:
                new_apps = Projects.objects.create(name=app, description="",image="home/static/img/Compressed168725-cloud-atmosphere-mountain-bedrock-mountainous-landforms_9GdAqR7.jpg", url=app)
        # else:   
        #     pprint("-------+1111-----")
            # apps_name = Projects.objects.all()
            # for a in apps_name:
            #     for app in apps:
            #         if str(a.name)==str(app) :
            #             app_name = Projects.objects.get(name=app)
            #             app_name.name=app
            #             app_name.description=""
            #             app_name.url=app
            #             app_name.save()
            #             pprint(a.name+"------SAVED")
                        
            #         else:
            #             pprint(a.name+"------NEW")
            #     pprint("------OBJECT")
            #     #new_apps = Projects.objects.create(name=app, description="",image="home/static/img/Compressed168725-cloud-atmosphere-mountain-bedrock-mountainous-landforms_9GdAqR7.jpg", url=app)
            # pprint("------ALWAYS")
            # #new_apps = Projects.objects.create(name=app, description="",image="home/static/img/Compressed168725-cloud-atmosphere-mountain-bedrock-mountainous-landforms_9GdAqR7.jpg", url=app)
                        
                        

                

            
        total_projects = Projects.objects.all().count()
        projects = Projects.objects.all()
        return render(request, "appGrid.html",
        context={
            "total_projects":total_projects,
            "projects":projects,
            "apps":apps,
            "username":username
            })
    else:
        return redirect('login')


def detail_project(request, id):
    if id:
        project = Projects.objects.filter(id_project=id)
        return render(request, "detail.html",{"project":project})

        # return HttpResponse(f"Yeahhh -----------{id}-----------{project} ")

    return HttpResponse(f"No se ha encontrado app con ese {id} ")