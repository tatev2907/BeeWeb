from django.core.management.base import BaseCommand, CommandError
from randomuser import RandomUser
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone
class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('count', type=int)

    def handle(self, *args, **options):
        user_list = RandomUser.generate_users(options['count'])

        for i in user_list:
            user = User()
            user.username = i.get_username()
            user.first_name = i.get_first_name()
            user.last_name = i.get_last_name()
            user.email = i.get_email()
            user.password = i.get_password()
            user.date_joined = datetime.now(tz=timezone.utc)
            user.save()
        self.stdout.write(self.style.SUCCESS(f'successfully published '))
