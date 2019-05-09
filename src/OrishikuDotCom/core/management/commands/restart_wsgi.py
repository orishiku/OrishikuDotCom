import os
import subprocess
from django.conf import settings
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Restart wsgi server'
    
    def handle(self, *args, **kwargs):
        subprocess.call(
            ["touch", os.path.join(
                settings.BASE_DIR,'OrishikuDotCom','wsgi','site.py')])
        subprocess.call(
            ["touch", os.path.join(
                settings.BASE_DIR,'OrishikuDotCom','wsgi','blog.py')])
        
        