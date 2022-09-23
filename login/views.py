from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def login(request):
    #return HttpResponse("Hello Login")
    return render(request, "loggin.html")

def index(request):
    return HttpResponse("Hello Login")
