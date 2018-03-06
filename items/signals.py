from .models import Item
from django.db import models
from haystack import signals


class ItemSignalProcessor(signals.BaseSignalProcessor):
    def setup(self):
        # Listen only to the ``Item`` model.
        models.signals.post_save.connect(self.handle_save, sender=Item)
        models.signals.post_delete.connect(self.handle_delete, sender=Item)

    def teardown(self):
        # Disconnect only for the ``Item`` model.
        models.signals.post_save.disconnect(self.handle_save, sender=Item)
        models.signals.post_delete.disconnect(self.handle_delete, sender=Item)
