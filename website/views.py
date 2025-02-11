from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request , 'website/index.html')

def about_me(request):
    return render(request , 'website/about.html')

def contact_me(request):
    return render(request , 'website/contact.html')