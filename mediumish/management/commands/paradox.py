from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Kluas is Immortal"

    def handle(self, *args, **options):
        print("Multiverse paradox")
