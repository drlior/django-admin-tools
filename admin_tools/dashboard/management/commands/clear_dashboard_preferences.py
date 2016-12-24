from django.core.management import BaseCommand

from admin_tools.dashboard.models import DashboardPreferences


class Command(BaseCommand):
    help = """Clears dashboard preferences."""

    def handle(self, *args, **options):
        DashboardPreferences.public_prepare_children.all().delete()
