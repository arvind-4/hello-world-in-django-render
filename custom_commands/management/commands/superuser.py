from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand, CommandError

from backend.env import config

DJANGO_SUPERUSER_PASSWORD = config("DJANGO_SUPERUSER_PASSWORD", default=None)
DJANGO_SUPERUSER_USERNAME = config("DJANGO_SUPERUSER_USERNAME", default=None)
DJANGO_SUPERUSER_EMAIL = config("DJANGO_SUPERUSER_EMAIL", default=None)

User = get_user_model()

class Command(BaseCommand):
    help = 'Creates a superuser.'
    def handle(self, *args, **options):
        try:
            user = User(
                email=DJANGO_SUPERUSER_EMAIL,
                username=DJANGO_SUPERUSER_USERNAME,
            )
            user.set_password(DJANGO_SUPERUSER_PASSWORD)
            user.is_active = True
            user.is_staff = True
            user.is_superuser = True
            user.is_admin = True
            user.save()
            print('Superuser has been created Successfully.')
        except Exception as e:
            print(e)