from django.urls import path
from . import views

app_name="home"

urlpatterns =[
    path("",views.index_home, name="home" ),
    path('<str:id>', views.detail_project, name='detail_project'),
    ]