from django.core.management.base import BaseCommand

from vorwaerts.models import ClassifiedAd
from vorwaerts.models import NewspaperPage


class Command(BaseCommand):
    def handle(self, *args, **options):
        NewspaperPage.objects.all().delete()
        ClassifiedAd.objects.all().delete()
