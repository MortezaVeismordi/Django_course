from django import template
from blog.models import Post
from blog.models import Category
from django.utils import timezone
#-----------------------------------------------------

register = template.Library()

#-----------------------------------------------------
@register.inclusion_tag('website/latest_post.html')
def latestposts():
    now = timezone.now()
    posts = Post.objects.filter(status=1 , published_date__lte=now).order_by('-published_date')[:6]
    return {'posts':posts}