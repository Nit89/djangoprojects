from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.

def display(request):
    return HttpResponse("<h1>My first django app for aneeshan</h1>")

def displayDateTime(request):
    dt=datetime.datetime.now()
    s="<b>current date is </b>"+str(dt)
    return HttpResponse(s)
    