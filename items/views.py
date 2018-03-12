from haystack.query import SearchQuerySet

from items.pagination import ItemLimitOffsetPagination
from .models import Item, ItemImage
from drf_haystack.viewsets import HaystackViewSet
from drf_haystack.filters import HaystackFilter
from .serializers import SearchSerializer, ItemSerializer, ImageSerializer, ItemSerializerUpdate
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.filters import OrderingFilter
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser, MultiPartParser
from rest_framework import permissions, status
from django.shortcuts import get_object_or_404
# from rest_framework.renderers import JSONRenderer


class ItemSearchView(HaystackViewSet):
    #  renderer_classes = (JSONRenderer,)  ############################# return raw json ###############################
    permission_classes = (permissions.IsAuthenticated,)

    index_models = [Item]
    # queryset = SearchQuerySet().exclude(validated=False) queryset ignored bug
    serializer_class = SearchSerializer
    pagination_class = ItemLimitOffsetPagination
    filter_backends = [HaystackFilter, OrderingFilter]
    ordering_fields = ('created', 'price')

    def get_queryset(self, index_models=[]):
        return super(ItemSearchView, self).get_queryset(index_models).filter(validated=True)


class ItemCreateView(APIView):
    parser_classes = (MultiPartParser, )
    permission_classes = (permissions.IsAuthenticated, )

    """
    create new item 
    """

    def post(self, request):
        #if request.user.is_authenticated():
        item_serializer = ItemSerializer(data=request.data, context={'request': request})
        if item_serializer.is_valid():
            new_item = item_serializer.save()  # item_serializer.save(owner=request.user)
            #if request.FILES is not None:
            for img in request.FILES.getlist('files'):
                ItemImage.objects.create(image=img, item=new_item)
            new_item.save()

            return Response(new_item.title)
        return Response(item_serializer.error_messages)


class ProfileItemListView(APIView):

    """
    list of all user's items
    """

    @staticmethod
    def get(request):
        profile_items = Item.objects.filter(owner=request.user)
        return Response(ItemSerializer(profile_items, many=True).data)


class ItemManageView(APIView):

    """
    update item 
    """

    @staticmethod
    def patch(request, item_id):
        item = get_object_or_404(Item, pk=item_id)
        serializer = ItemSerializerUpdate(item, data=request.data, context={'request': request}, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(ItemSerializer(serializer.instance).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    """
    delete item 
    """

    @staticmethod
    def delete(request, item_id):

        # item = Item.objects.filter(pk=item_id)
        item = get_object_or_404(Item, pk=item_id)
        if item.owner != request.user:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





