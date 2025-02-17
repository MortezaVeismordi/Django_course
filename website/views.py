from django.http import HttpResponse
from django.shortcuts import render
from website.models import Contact
from website.forms import NameForm , ContactForm

#---------------------------------------------------------------------

def index(request):
    return render(request , 'website/index.html')

def about_me(request):
    return render(request , 'website/about.html')

def contact_me(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
    form = ContactForm
    return render(request , 'website/contact.html' , {'form':form})

def test_view(request):
    if request.method =='POST':
        name = request.POST.get("name")
        form = NameForm(request.POST)
        
    return render(request , 'test.html' , {'name': 'Morteza'})