from rest_framework import serializers
from .search_indexes import ItemIndex
from drf_haystack.serializers import HaystackSerializer
from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer, HyperlinkedIdentityField
from items.models import Item, ItemImage


class ItemSerializer(ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Item
        fields = '__all__'


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
            "owner_name",
            "owner_photo",
            "owner_id",
            "title",
            "body",
            "price",
            "category",
            "phone",
            "location",
            'size',
            'color',
            'condition',
            'delivery',
            'promotion',
            'rent',
            'wholesale',
            'views',
            "created",
            "validated",
            "id",
            "photos",
            "likes"
        ]


class ItemSerializerUpdate(serializers.ModelSerializer):

    class Meta:
        model = Item
        exclude = ('owner',)

    def validate(self, data):
        """
        Validate authenticated user
        """

        if self.instance.owner != self.context['request'].user:
            raise serializers.ValidationError('You can not edit posts from other users')
        return data
