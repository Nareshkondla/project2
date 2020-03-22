from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def tussu(request):
    return  HttpResponse("<h1>tussu, Come to game<h1/>")
def tharu(request):
    return  HttpResponse("<h1>Hi Tharun <h1/>")
def chandu(request):
    return  HttpResponse("<h1>Hi Chandu<h1/>")
