from django.contrib import admin
from testapp.models import Story,Comment

class StoryAdmin(admin.ModelAdmin):
    list_display=['title','author','publish','created','updated','status']
    list_filter=['status','author','created','publish']
    search_fields=['title','body']

    date_hierarchy='publish'
    prepopulated_fields={'slug':('title',)}
class CommentAdmin(admin.ModelAdmin):
    list_display=['name','email','cmnt','created','updated','story','active']
    list_filter=['name','email']
    search_fields=['name','email']

    date_hierarchy='created'

# Register your models here.

admin.site.register(Story,StoryAdmin)
admin.site.register(Comment,CommentAdmin)
