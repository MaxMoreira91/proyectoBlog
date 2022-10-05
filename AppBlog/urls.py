from django.contrib import admin
from django.urls import path
from AppBlog.views import *

urlpatterns = [
    path("integrantes/", Integrante),
    path("post/", Post),
]