from django.shortcuts import render , get_object_or_404
from django.utils import timezone
from blog.models import Post
from blog.models import Category
# Create your views here.
def blog_view(request , cat_name=None):
    now = timezone.now()
    posts = Post.objects.filter(status = 1 , published_date__lte = now).order_by('-published_date')
    if cat_name:
        posts = posts.filter(category__name=cat_name)
    context = {'posts':posts }
    return render(request , "blog/blog-home.html" , context)

def blog_single (request , pid):
    now = timezone.now()
    post = get_object_or_404(Post , pk=pid , status = 1 , published_date__lte=now)
    post.counted_views += 1
    post.save()
    previous_post = Post.objects.filter(status = 1 ,published_date__lt=post.published_date , published_date__lte=now).order_by('-published_date').first()
    next_post = Post.objects.filter(status = 1 ,published_date__gt=post.published_date , published_date__lte=now).order_by('published_date').first()
    context = {
        'post': post,
        'previous_post': previous_post,
        'next_post': next_post,
    }
    return render(request , 'blog/blog-single.html' , context)


def blog_category(request , cat_name):
    posts = Post.objects.filter(status=1)
    posts = posts.filter(category__name=cat_name)
    context = {'posts':posts }
    return render(request , "blog/blog-home.html" , context)






def test(request , pid):
    post = get_object_or_404(Post , pk=pid)
    context = {'post':post }
    return render(request , 'test.html', context)
