from django.contrib.sites.models import Site
from django.contrib.flatpages.models import FlatPage
from django.db import models
from django.urls import get_script_prefix
from django.utils.encoding import iri_to_uri
from django.utils.translation import gettext_lazy as _

class Page(FlatPage):
    in_main_menu = models.BooleanField(
        _('show in main menu'),
        help_text=_("If this is checked, the page will be visible in main menu."),
        default=False,
    )
    
    class Meta:
        verbose_name = _('page')
        verbose_name_plural = _('pages')
        db_table = 'dapricot_pages_page'
