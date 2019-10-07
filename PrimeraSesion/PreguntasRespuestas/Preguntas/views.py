from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hola mamagueva. Bienvenidos a EciTech")


# Create your views here.
