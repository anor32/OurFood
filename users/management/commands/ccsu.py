
from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        admin_user = User.objects.create(
            email="admin@web.top",
            first_name="Andrei",
            last_name="Nikanov",
            role='admin',
            phone='+89999999',
            address='Улица пушкина дом колотушкина',
            is_staff=True,
            is_superuser=True,
            is_active=True,

        )
        admin_user.set_password("querty")
        admin_user.save()
        print("admin_created")

        moderator = User.objects.create(
            email="moder@web.top",
            first_name="Moder",
            last_name="Moderatorov",
            role='moderator',
            phone='+89999999',
            address='Улица пушкина дом колотушкина',
            is_staff=True,
            is_superuser=False,
            is_active=True,

        )

        moderator.set_password('qwerty')
        moderator.save()
        print('Moderator Created')

        user = User.objects.create(
            email="user@web.top",
            first_name="user",
            last_name="userov",
            role='user',
            phone='+89999999',
            address='Улица пушкина дом колотушкина',

            is_staff=False,
            is_superuser=False,
            is_active=True,

        )
        user.set_password('qwerty')
        user.save()
        print('user Created')