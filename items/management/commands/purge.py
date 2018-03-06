from django.core.management.base import BaseCommand, CommandError
from items.models import Item
from datetime import datetime, timedelta
from django.utils import timezone
import pytz


class Command(BaseCommand):
    help = 'Delete objects older than 3 months'

    def handle(self, *args, **options):
        # Item.objects.filter(created__gte=timezone.now()-timedelta(hours=1)).delete()

        tz = pytz.timezone('Africa/Algiers')
        Item.objects.filter(created__lte=datetime.now(tz)-timedelta(days=1)).delete()
        self.stdout.write('Deleted objects older than 3 months')
