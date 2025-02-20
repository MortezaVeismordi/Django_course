from django.shortcuts import render , get_object_or_404
from django.utils import timezone
from blog.models import Post , Coment
from blog.models import Category
from django.core.paginator import Paginator , EmptyPage , PageNotAnInteger


def blog_view(request , **kwargs):
    now = timezone.now()
    posts = Post.objects.filter(status = 1 , published_date__lte = now).order_by('-published_date')
    if kwargs.get('cat_name') :
        posts = posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('author_username'):
        posts = posts.filter(author__username = kwargs['author_username'])
    if kwargs.get('tag_name'):
        posts = posts.filter(tags__name__in=[kwargs['tag_name']])
        
    posts=Paginator(posts , 3)
    try:
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)

    context = {'posts':posts }
    return render(request , "blog/blog-home.html" , context)



def blog_single (request , pid):
    now = timezone.now()
    post = get_object_or_404(Post , pk=pid , status = 1 , published_date__lte=now)
    post.counted_views += 1
    post.save()
    comments = Coment.objects.filter(post=post.id , approved = True).order_by('-created_date')
    previous_post = Post.objects.filter(status = 1 ,published_date__lt=post.published_date , published_date__lte=now).order_by('-published_date').first()
    next_post = Post.objects.filter(status = 1 ,published_date__gt=post.published_date , published_date__lte=now).order_by('published_date').first()
    context = {
        'post': post,
        'previous_post': previous_post,
        'next_post': next_post,
        'comments':comments,
    }
    return render(request , 'blog/blog-single.html' , context)



def blog_category(request , cat_name):
    posts = Post.objects.filter(status=1)
    posts = posts.filter(category__name=cat_name)
    context = {'posts':posts }
    return render(request , "blog/blog-home.html" , context)



def blog_search(request):
    posts = Post.objects.filter(status = 1)
    if request.method == 'GET':
        posts = posts.filter(content__contains =request.GET.get('s'))    
    context = {'posts':posts }
    return render(request , "blog/blog-home.html" , context)



def test(request , pid):
    post = get_object_or_404(Post , pk=pid)
    context = {'post':post }
    return render(request , 'test.html', context)
