from haystack import indexes
from django.utils import timezone
from .models import Item
from django.db import models


class ItemIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    owner_name = indexes.CharField()
    owner_photo = indexes.CharField()
    owner_id = indexes.IntegerField()

    title = indexes.CharField(model_attr="title")
    body = indexes.CharField(model_attr="body")
    price = indexes.IntegerField(model_attr="price")
    category = indexes.CharField(model_attr="category")
    phone = indexes.CharField(model_attr="phone")
    location = indexes.CharField(model_attr="location")

    size = indexes.CharField(model_attr="size")
    color = indexes.CharField(model_attr="color")

    condition = indexes.BooleanField(model_attr='condition')
    delivery = indexes.BooleanField(model_attr='delivery')
    promotion = indexes.BooleanField(model_attr='promotion')
    rent = indexes.BooleanField(model_attr='rent')
    wholesale = indexes.BooleanField(model_attr='wholesale')

    likes = indexes.IntegerField(model_attr='likes')
    views = indexes.IntegerField(model_attr='views')

    created = indexes.FacetDateTimeField(model_attr="created")
    validated = indexes.BooleanField(model_attr='validated')
    id = indexes.IntegerField(model_attr="id")
    photos = indexes.MultiValueField()

    # autocomplete = indexes.EdgeNgramField()

    def prepare_owner_name(self, obj):
        return obj.owner.user_name

    def prepare_owner_photo(self, obj):
        return obj.owner.image_url

    def prepare_owner_id(self, obj):
        return obj.owner.id

    def prepare_photos(self, obj):
        return [img.image.url for img in obj.images.all()]

    def get_model(self):
        return Item

    def index_queryset(self, using=None):
        return self.get_model().objects.filter(
            created__lte=timezone.now()
        )

    # def get_queryset(self):
    #     return self.get_model().objects.all().exclude(validated=False)
