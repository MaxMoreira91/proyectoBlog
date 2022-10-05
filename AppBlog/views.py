from django.shortcuts import render
from .models import *
from django.http import HttpResponse




def Integrante(request):
    return render (request, "AppBlog/Integrates.html")

def Post(request):
    return render(request, "AppBlog/Post.html")

def Inicio(request):
    return render (request, "AppBlog/inicio.html")