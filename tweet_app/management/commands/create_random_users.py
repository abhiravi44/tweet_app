from django.core.management.base import BaseCommand
from django.utils import timezone
from tweet_app.models import User
from django.utils.crypto import get_random_string
import random 

class Command(BaseCommand):
    help = 'Create random users'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Indicates the number of users to be created')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        for i in range(total):
            User.objects.create_user(username=get_random_string(), email='', password='123456',mobile='9000100'+str(random.randint(100,999)))
