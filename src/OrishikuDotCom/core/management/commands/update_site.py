import os
from git import Repo
from django.core.management.base import BaseCommand
from OrishikuDotCom.settings.utils import ConfigFile

class Command(BaseCommand):
    help = 'Update site project from git'
    
    def add_arguments(self, parser):
            parser.add_argument('repository_path', type=str, help='Indicates the path of the repository to work')

    def handle(self, *args, **kwargs):
        repository_path = kwargs['repository_path']
        repo = Repo(repository_path)
        o = repo.remotes.origin
        #hello
        repo.git.stash()
        o.fetch()
        repo.git.checkout('develop')
        o.pull
        repo.git.stash('pop')
        