from pprint import pprint
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User




# Create your views here.
def login(request):
    users = User.objects.all()
    super = User.objects.filter(is_superuser=1)
    pprint(super)
    return render(request, "loggin.html", {"super":super, "users":users})

def index(request):
    return HttpResponse("Hello Login")
