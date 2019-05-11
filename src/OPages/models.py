from django.contrib.sites.models import Site
from django.contrib.flatpages.models import FlatPage
from django.db import models
from django.urls import get_script_prefix
from django.utils.encoding import iri_to_uri
from django.utils.translation import gettext_lazy as _

class Page(FlatPage):
    pass
