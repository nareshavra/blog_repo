from django.shortcuts import render,get_object_or_404
from testapp.models import Story
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from testapp.forms import CommentForm
from taggit.models import Tag
# Create your views here.
def home(request,tag_slug=None):
    stories=Story.objects.all()
    tag=None
    if tag_slug:
        tag=get_object_or_404(Tag,slug=tag_slug)
        stories=stories.filter(tags__in=[tag])
    paginator=Paginator(stories,4)
    page_number=request.GET.get('page')
    try:
        stories=paginator.page(page_number)
    except PageNotAnInteger:
        stories=paginator.page(1)
    except EmptyPage:
        stories=paginator.page(paginator.num_pages)

    return render(request,'testapp/home.html',{'stories':stories,'tag':tag})
def StoryDetailView(request,year,month,day,story):
    story=get_object_or_404(
    Story,
    slug=story,
    status='published',
    publish__year=year,
    publish__month=month,
    publish__day=day
    )
    stories=Story.objects.all()
    comments=story.comments.filter(active=True)
    csubmit=False
    if request.method=='POST':
        form=CommentForm(request.POST)
        if form.is_valid():
            new_comment=form.save(commit=False)
            new_comment.story=story
            new_comment.save()
            csubmit=True
    else:
        form=CommentForm()




    return render(request,'testapp/storydetail.html',{'story':story,'form':form,'csubmit':csubmit,'comments':comments})
