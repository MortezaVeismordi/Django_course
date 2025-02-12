from django.shortcuts import render

# Create your views here.
def blog_view(request):
    return render(request , "blog/blog-home.html")

def blog_single (request):
    context = {'name':'Mori love Masi <3' , 'content':'Mori always love masi' , 'author' : 'Morteza'}
    return render(request , 'blog/blog-single.html' , context)