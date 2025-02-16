from django.shortcuts import render , get_object_or_404
from django.utils import timezone
from blog.models import Post
# Create your views here.
def blog_view(request):
    now = timezone.now()
    posts = Post.objects.filter(status = 1 , published_date__lte = now).order_by('-published_date')
    context = {'posts':posts }
    return render(request , "blog/blog-home.html" , context)

def blog_single (request , pid):
    post = get_object_or_404(Post , pk=pid)
    post.counted_views += 1
    post.save()
    context = {'post':post }
    return render(request , 'blog/blog-single.html' , context)



def test(request , pid):
    # now = timezone.now()
    # post = Post.objects.filter(published_date__lte = now).order_by('-published_date')
    post = get_object_or_404(Post , pk=pid)
    context = {'post':post }
    return render(request , 'test.html', context)
