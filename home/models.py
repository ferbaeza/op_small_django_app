from distutils.command.upload import upload
from email.policy import default
from django.db import models
from uuid import uuid4
from pprint import pprint
from django.conf import settings

def get_app_installed():
    apps = settings.INSTALLED_APPS
    lista_apps=[]
    pprint("-----------Apps instaladas-----------------")
    for a in apps:
        a = a.split(".")
        if a[0] != "django":
            pprint(a)
            lista_apps.append(a[0])
    #pprint(lista_apps)
    pprint(f"Lista apps instaladas {lista_apps}")
    pprint("-------------------------------------------")
    #TODO Insert this apps into db 

    return lista_apps

t= get_app_installed()










class Projects(models.Model):
    id_project = models.UUIDField(primary_key=True, default=uuid4, help_text="Apps creadas")
    name = models.CharField(max_length=100, help_text="App_Name")
    description = models.TextField(max_length=1111,blank=True, null=True, help_text="Descripcion de la app")
    image = models.ImageField(default="", upload_to="home/static/images")
    url = models.CharField(max_length=100)
    img = models.URLField(default="", blank=True)


    def __str__(self) -> str:
        return self.name    


