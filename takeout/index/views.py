#system

#django
from django.shortcuts import render

#mysetting
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("hello")