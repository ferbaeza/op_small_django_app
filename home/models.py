from django.db import models
from uuid import uuid4
from pprint import pprint
from django.conf import settings




class Projects(models.Model):
    id_project = models.UUIDField(primary_key=True, default=uuid4, help_text="Apps creadas")
    name = models.CharField(max_length=100, help_text="App_Name")

    def get_app_installed(self):
        apps = settings.INSTALLED_APPS
        lista_apps=[]
        pprint("-----------Apps instaladas-----------------")
        for a in apps:
                a = a.split(".")
                if a[0] != "django":
                    pprint(a)
                    lista_apps.append(a)
        #pprint(lista_apps)
        pprint("-------------------------------------------")
        #TODO Insert this apps into db 
        return lista_apps

    t= get_app_installed(name)

    def __str__(self) -> str:
        return self.name