from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request , 'index.html')

def about_me(request):
    return HttpResponse('<h1> about me <h1')

def contact_me(request):
    return HttpResponse('<h1> Number <h1')