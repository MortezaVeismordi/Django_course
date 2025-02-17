from django import template
from blog.models import Post
from blog.models import Category

#-----------------------------------------------------

register = template.Library()

#-----------------------------------------------------
@register.inclusion_tag('website/latest_post.html')
def latestposts():
    posts = Post.objects.filter(status=1).order_by('-published_date')
    return {'posts':posts}