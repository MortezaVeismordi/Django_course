from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1> Home page <h1')

def about_me(request):
    return HttpResponse('<h1> about me <h1')

def contact_me(request):
    return HttpResponse('<h1> Number <h1')