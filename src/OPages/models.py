from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.flatpages.models import FlatPage

class Page(FlatPage):
    in_main_menu = models.BooleanField(_('view in main menu'), default=False)
