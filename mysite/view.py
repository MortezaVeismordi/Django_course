from django.http import HttpResponse

def http_test(request):
    return HttpResponse('h1> Hello <h1')
