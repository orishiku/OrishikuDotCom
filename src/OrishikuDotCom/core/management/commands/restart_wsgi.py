import os
import subprocess
from django.conf import settings
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Restart wsgi server'
    
    def handle(self, *args, **kwargs):
        wsgi_path = os.path.join(settings.BASE_DIR,'OrishikuDotCom','wsgi')
        print(wsgi_path);
        subprocess.call(["touch",os.path.join(wsgi_path,'site.py')])
        subprocess.call(["touch",os.path.join(wsgi_path,'blog.py')])
        
        
        