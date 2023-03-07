from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def deviFirst(request):
    return HttpResponse('<h1>DEVIPRASAD1</h1>')


def deviSecond(request):
    return HttpResponse('<h1>DEVIPRASAD2</h1>')