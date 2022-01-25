# core urls file here

from django.contrib import admin
from django.urls import path,include
# from django.http import HttpResponse


# this is a function which takes requwst object and returns httpresponse


# def home(request):
#     return HttpResponse('HOME PAGE')

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',home)
    path('',include('base.urls')),
    path('',include('collector.urls')),
]
