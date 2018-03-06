from haystack import indexes
from django.utils import timezone
from .models import Item
from django.db import models


class ItemIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    title = indexes.CharField(model_attr="title", faceted=True)
    body = indexes.CharField(model_attr="body", faceted=True)
    price = indexes.IntegerField(model_attr="price")
    category = indexes.CharField(model_attr="category", faceted=True)
    sub_category = indexes.CharField(model_attr="sub_category", faceted=True)
    phone = indexes.CharField(model_attr="phone", faceted=True)
    location = indexes.CharField(model_attr="location", faceted=True)
    created = indexes.FacetDateTimeField(model_attr="created")
    likes = indexes.IntegerField(model_attr='likes')
    validated = indexes.BooleanField(model_attr='validated')
    id = indexes.CharField(model_attr="id")
    photos = indexes.MultiValueField()

    # autocomplete = indexes.EdgeNgramField()

    def prepare_photos(self, obj):
        return [img.image.url for img in obj.images.all()]

    @staticmethod
    def prepare_autocomplete(obj):
        return " ".join(obj.title)

    def get_model(self):
        return Item

    def index_queryset(self, using=None):
        return self.get_model().objects.filter(
            created__lte=timezone.now()
        )

