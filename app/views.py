from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def My_name(request):
    return HttpResponse('<marquee><h1>Yeh Dil Mange More<h1/></marquee>')