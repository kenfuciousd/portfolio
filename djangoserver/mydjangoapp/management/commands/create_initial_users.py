from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Create initial users'

    def handle(self, *args, **kwargs):
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@example.com', '@dm1n1str4t0r')
            self.stdout.write(self.style.SUCCESS('Successfully created superuser "admin"'))

        if not User.objects.filter(username='guest_courier').exists():
            User.objects.create_user('guest_courier', 'courier@example.com', 'P@ssw0rd!')
            self.stdout.write(self.style.SUCCESS('Successfully created user "guest_courier"'))

        if not User.objects.filter(username='guest_customer').exists():
            User.objects.create_user('guest_customer', 'customer@example.com', 'P@ssw0rd!')
            self.stdout.write(self.style.SUCCESS('Successfully created user "guest_customer"'))
