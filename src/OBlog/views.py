from django.http import Http404
from django.shortcuts import render
from OBlog.models import Post, Category, Tag

def post(request, day, month, year, slug):
    post = Post.objects.filter(status='p')
    
    post.filter(publish_date__year=year,
                publish_date__month=month,
                publish_date__day=day)
    
    for p in post:
        if p.slug==slug:
            return render(request, 'blog/post.html')
    
    raise Http404("Post does not exist")

def filterList(request, filter_name):
    
    if filter_name=='category':
        filter_list = Category.objects.all()
    elif filter_name=='tag':
        filter_list = Tag.objects.all()
    
    if filter_list:
        return render(request, 'blog/filter_list.html', {'filter_list':filter_list})
    
    raise Http404("Poll does not exist")

def postList(request, filter_name, value):
    post_list = Post.objects.filter(status='p')
        
    if filter_name=='category':
        post_list = Post.objects.filter(category__name=value)
    elif filter_name=='tag':
        post_list.filter(tag__name=value)
    
    if post_list.count()>0:
        return render(request, 'blog/post_list.html', {'post_list':post_list,})
    
    raise Http404("Poll does not exist")
