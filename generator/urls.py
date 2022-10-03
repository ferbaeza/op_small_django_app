from django.urls import path
from . import views

app_name="generator"

urlpatterns = [
    path('', views.home, name='generator'),
    path('about',views.about, name='about'),
    path('password', views.password, name='password')
]
