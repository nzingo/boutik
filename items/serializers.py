from rest_framework import serializers
from .search_indexes import ItemIndex
from drf_haystack.serializers import HaystackSerializer
from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer, HyperlinkedIdentityField
from items.models import Item, ItemImage


class ItemSerializer(ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Item
        fields = [
            'owner',
            'title',
            'body',
            'price',
            'category',
            'sub_category',
            'phone',
            'location',
            'created',
            'validated',
            'id'
        ]


class ImageSerializer(ModelSerializer):
    class Meta:
        model = ItemImage
        fields = [
            'image',
            'item'
        ]


class SearchSerializer(HaystackSerializer):

    class Meta:
        index_classes = [ItemIndex]
        fields = [
            "title",
            "body",
            "price",
            "category",
            "sub_category",
            "phone",
            "location",
            "created",
            "validated",
            "id",
            "photos",
            "likes"
        ]
