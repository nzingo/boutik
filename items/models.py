from django.db import models
from django.conf import settings
from django.db.models.signals import post_delete
from django.dispatch.dispatcher import receiver
#from gdstorage.storage import GoogleDriveStorage

# Define Google Drive Storage
# gd_storage = GoogleDriveStorage()


class Item(models.Model):

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    title = models.CharField(max_length=50)
    body = models.TextField()

    price = models.IntegerField()   # eleminate "null=true" after deleting migrations
    category = models.CharField(max_length=50)  # one category "woman clothes dresses"
    phone = models.CharField(max_length=50)
    location = models.CharField(max_length=50)  # one location "alger bab ezzouar"

    size = models.CharField(max_length=50)
    color = models.CharField(max_length=50)

    condition = models.BooleanField()
    delivery = models.BooleanField()
    promotion = models.BooleanField()
    rent = models.BooleanField()
    wholesale = models.BooleanField()

    likes = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    validated = models.BooleanField(default=False)

    def __str__(self):
        return "%s" % self.title


class ItemImage(models.Model):
    item = models.ForeignKey(Item, null=True, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField()
    # image = models.ImageField(upload_to='images', storage=gd_storage)

    def __str__(self):
        return "%s" % self.image.name

# delete images frome drive when object deleted
@receiver(post_delete, sender=ItemImage)
def itemimage_delete(sender, instance, **kwargs):
    if instance.image:
        instance.image.delete(False)

