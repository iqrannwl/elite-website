from django.core.management.base import BaseCommand
from accounts.models import User


class Command(BaseCommand):
    help = 'Set password for admin user'

    def handle(self, *args, **options):
        try:
            admin = User.objects.get(username='admin')
            admin.set_password('admin123')
            admin.role = User.UserRole.SUPER_ADMIN
            admin.save()
            self.stdout.write(self.style.SUCCESS('Successfully set admin password to: admin123'))
        except User.DoesNotExist:
            self.stdout.write(self.style.ERROR('Admin user does not exist'))
