from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=125)
    subject = models.CharField(max_length=255 , blank=True,null=True)
    email = models.EmailField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('created_at' ,)
    def __str__(self):
        return self.name

