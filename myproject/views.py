#from django.http import HttpResponse;
from django.shortcuts import render;

def homepage(request):
    #return HttpResponse("Hello world! This is home.")
    return render(request, 'home.html')


def aboutpage(request):
    #return HttpResponse("This is about us")
    return render(request, 'about.html')