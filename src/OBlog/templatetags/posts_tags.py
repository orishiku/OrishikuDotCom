from django import template
from OBlog.models import Post, Category, Tag

register = template.Library()

@register.simple_tag
def posts_in_category(category_slug, limit=None):
    categories = Category.objects.all()
    posts = Post.objects.filter(status='p').order_by('-publish_date')
    filter_applied = False
    for c in categories:
        if c.slug==category_slug:
            posts = posts.filter(category__name=c.name)
            filter_applied = True
    if filter_applied:
        if limit:
            return posts[:limit]
        else:
            return posts
    else:
        return None