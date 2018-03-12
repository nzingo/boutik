from django.conf.urls import url, include
from rest_framework import routers
from items.views import ItemSearchView, ItemCreateView, ProfileItemListView, ItemManageView


router = routers.DefaultRouter()
router.register("search", ItemSearchView, base_name="item-search")

urlpatterns = [
    url(r"^", include(router.urls)),
    url(r'^create/$', ItemCreateView.as_view(), name='create'),
    url(r'^profile-items/$', ProfileItemListView.as_view(), name='profile items'),
    url(r'^manage-items/(?P<item_id>\d+)/$', ItemManageView.as_view(), name='manage items'),
]