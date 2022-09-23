from django.urls import path
from . import views

app_name="appStore"


urlpatterns = [
    path("", views.index, name="appStore")
]
