from django.contrib import admin
from blog.models import Post , Category , Coment
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.

class PostAdmin(SummernoteModelAdmin):
    date_hierarchy = 'created_at'
    empty_value_display = '-empty-'
    list_display = ('title' ,'author' ,'counted_views' , 'published_date' , 'created_at' , 'updated_time')
    list_filter = ('status' , 'author')
    #ordering = ['created_at']
    search_fields = ['title' , 'content']
    summernote_fields =('content',)

class ComentAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('name' ,'email' ,'subject' , 'message' , 'approved' , 'created_date' , 'updated_date')
    list_filter = ('post' , 'approved')
    search_fields = ['title' , 'content']

admin.site.register(Coment , ComentAdmin)
admin.site.register(Category)
admin.site.register(Post , PostAdmin)