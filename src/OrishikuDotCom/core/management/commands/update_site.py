import os
from git import Repo
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Update site project from git'
    
    def add_arguments(self, parser):
            parser.add_argument('repository_path', type=str, help='Indicates the path of the repository to work')

    def handle(self, *args, **kwargs):
        repository_path = kwargs['repository_path']
        repo = Repo(repository_path)

        repo.git.fetch('--all')
        repo.git.reset('--hard','origin/release/alpha')
        