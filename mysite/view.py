from django.http import HttpResponse
from django.shortcuts import render

def http_test(request):
    return HttpResponse('h1> Hello <h1')

def under_construction(request):
    return render(request, "coming_soon.html")
