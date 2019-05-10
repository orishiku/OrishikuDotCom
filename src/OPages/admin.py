from django.contrib import admin
from django.contrib.flatpages.models import FlatPage
from django.utils.translation import ugettext_lazy as _
from OPages.models import Page

admin.site.unregister(FlatPage)

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('url', 'title', 'content', 'sites')}),
        (_('Advanced options'), {'classes': ('collapse',),
        'fields': ('enable_comments', 'registration_required', 'template_name')}),
    )
    list_display = ('url', 'title')
    list_filter = ('sites', 'enable_comments', 'registration_required')
    search_fields = ('url', 'title')
