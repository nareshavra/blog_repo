from django import template
from testapp.models import Story
from django.db.models import Count
register=template.Library()
@register.simple_tag
def total_posts():

    return Story.objects.count()
@register.inclusion_tag('testapp/latestposts123.html')
def show_posts(count=3):
    latest_posts=Story.objects.order_by('-publish')[:count]
    return {'latest_posts':latest_posts}
@register.simple_tag
def most_commented_post(count=3):
    return Story.objects.annotate(total_comments=Count('comments')).order_by('-total_comments')[:count]
