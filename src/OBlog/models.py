from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.html import strip_tags
from django.conf import settings
from django.utils.text import slugify
from django.contrib.sites.models import Site
from django.utils.safestring import mark_safe

ENTRY_STATUS_OPTIONS = (
    ('d','Draft'),
    ('p','Published'),
)

class Post(models.Model):
    title        = models.CharField(max_length=100)
    content      = models.TextField()
    side_content = models.TextField(null=True)
    #cover         = models.models.ForeignKey('Media', on_delete=models.CASCADE)
    
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    status   = models.CharField(choices=ENTRY_STATUS_OPTIONS, max_length=1)
    
    tags = models.ManyToManyField('Tag')
    
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, editable=False)
    
    #is_iced       = models.BooleanField(default=False, editable=False)
    creation_date = models.DateTimeField(auto_now_add=True, editable=False)
    edit_date     = models.DateTimeField(auto_now=True, editable=False)
    publish_date  = models.DateTimeField(editable=False, null=True)
    
    @property
    def get_preview(self):
        preview_content = self.content.split('</p>')
        preview_content = strip_tags(preview_content[0])
        preview_content = preview_content[0:1000]
        #cleaned_content = strip_tags(self.content)
        return preview_content
    
    @property
    def slug(self):
        t = slugify(self.title)[0:40]
        id = self.id
        return "{0}_{1}".format(t, id)
    
    @property
    def permalink(self):
        current_site = Site.objects.get_current()
        date=self.publish_date
        if date != None:
            permalink = '/{0}/{1}/{2}/{3}'.format(
                date.day, date.month, date.year,
                self.slug)
            url = "<a href='{1}'>{1}</a>".format(
                current_site,permalink)
            return mark_safe(url)
        else:
            return None
    class Meta:
        verbose_name = _('post')
        verbose_name_plural = _('posts')
        ordering = ('creation_date',)

    def __str__(self):
        return "%s -- %s" % (self.title, self.author)

class Category(models.Model):
    name = models.CharField(max_length=50)

    @property
    def slug(self):
        return slugify(self.name)
    
    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=50)
    
    @property
    def slug(self):
        return slugify(self.name)
    
    class Meta:
        verbose_name = _('tag')
        verbose_name_plural = _('tags')

    def __str__(self):
        return self.name
    