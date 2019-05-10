from django.http import Http404
from django.shortcuts import render
from django.core.paginator import Paginator

from OBlog.models import Post, Category, Tag

def post(request, day, month, year, slug):
    post = Post.objects.filter(publish_date__year=year,
                publish_date__month=month,
                publish_date__day=day,
                status='p')
    
    for p in post:
        if p.slug==slug:
            return render(request, 'blog/post.html', {
                'post': p,
                })
    
    raise Http404("Post does not exist")

def filterList(request, filter_name):
    
    if filter_name=='category':
        filter_list = Category.objects.all()
    elif filter_name=='tag':
        filter_list = Tag.objects.all()
    
    if filter_list:
        return render(request, 'blog/filter_list.html', {
            'filter_list':filter_list,
            'filter_name': filter_name
        })
    
    raise Http404("Poll does not exist")

def postList(request, filter_name=None, value=None, page=1):
    post_list = Post.objects.filter(status='p').order_by('-publish_date')
    filter_value = None
    if filter_name=='category':
        categories = Category.objects.all()
        for c in categories:
            if c.slug==value:
                filter_value = c
        post_list = post_list.filter(category__name=filter_value.name)
        
    elif filter_name=='tag':
        tags = Tag.objects.all()
        
        for t in tags:
            if t.slug==value:
                filter_value = t
        post_list = post_list.filter(tags__name=filter_value.name)
    
    paginator = Paginator(post_list, 10)
    list_page = paginator.get_page(page)
    
    data = { 'post_list':list_page }
    template = 'blog/main_site.html'
    
    if filter_name:
        data.update({ 'filter': [filter_name, filter_value] })
        template = 'blog/post_list.html'
        
    return render(request, template, {
        'post_list':list_page,
        'filter': [filter_name, filter_value]
    })
    
    raise Http404("Poll does not exist")
