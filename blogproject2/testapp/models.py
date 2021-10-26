from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from taggit.managers import TaggableManager

# Create your models here.
class CustomManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='published')

class Story(models.Model):
    STATUS_CHOICES=(('published','Published'),('draft','Draft'))
    author=models.ForeignKey(User,related_name='story_posts',on_delete=models.CASCADE)
    title=models.CharField(max_length=264)
    body=models.TextField()
    image=models.ImageField(blank=True,upload_to='blog_images')
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    publish=models.DateTimeField(default=timezone.now)
    slug=models.SlugField(max_length=264,unique_for_date='publish')
    status=models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')
    objects=CustomManager()
    tags=TaggableManager()

    class Meta:
        ordering=('-publish',)
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('story_details',args=[self.publish.year,self.publish.strftime('%m'),self.publish.strftime('%d'),self.slug])
class Comment(models.Model):
    story=models.ForeignKey(Story,related_name='comments',on_delete=models.CASCADE)
    name=models.CharField(max_length=32)
    email=models.EmailField()
    cmnt=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)

    class Meta:
        ordering=('-created',)
