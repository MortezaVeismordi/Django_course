from django.db import models

# Create your models here.
class Post(models.Model):
    # image
    # author
    title = models.CharField(max_length=125)
    content = models.TextField()
    # tag
    # category
    counted_views = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
    def __str__(self):
        return '{} - {}'.format(self.title , self.id)
    
