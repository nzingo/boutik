from items.pagination import ItemLimitOffsetPagination
from .models import Item, ItemImage
from drf_haystack.viewsets import HaystackViewSet
from drf_haystack.filters import HaystackFilter
from .serializers import SearchSerializer, ItemSerializer, ImageSerializer
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.filters import OrderingFilter
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser, MultiPartParser
# from rest_framework.renderers import JSONRenderer


class ItemSearchView(HaystackViewSet):
    #  renderer_classes = (JSONRenderer,)  ############################# return raw json ###############################

    index_models = [Item]
    # queryset = Item.objects.exclude(validated=False)
    serializer_class = SearchSerializer
    pagination_class = ItemLimitOffsetPagination
    filter_backends = [HaystackFilter, OrderingFilter]
    ordering_fields = ('created', 'price')


class CustomCreateView(APIView):
    parser_classes = (MultiPartParser, )

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







