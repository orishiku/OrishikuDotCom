from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.html import strip_tags
from django.conf import settings
from django.utils.text import slugify

ENTRY_STATUS_OPTIONS = (
    ('d','Draft'),
    ('p','Published'),
)

class Post(models.Model):
    title        = models.CharField(max_length=50)
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
        cleaned_content = strip_tags(self.content)
        return cleaned_content[0:1000]
    
    @property
    def slug(self):
        permalink = "{0}_{1}".format(
            slugify(self.publish_date)[0:10],
            slugify(self.title)[0:40])
        return permalink
    
    class Meta:
        verbose_name = _('post')
        verbose_name_plural = _('posts')
        ordering = ('creation_date',)

    def __str__(self):
        return "%s -- %s" % (self.title, self.author)

class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=50)
    
    class Meta:
        verbose_name = _('tag')
        verbose_name_plural = _('tags')

    def __str__(self):
        return self.name
    