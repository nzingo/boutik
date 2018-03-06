from django.conf.urls import url, include
from rest_framework import routers
from items.views import ItemSearchView, CustomCreateView


router = routers.DefaultRouter()
router.register("search", ItemSearchView, base_name="item-search")

urlpatterns = [
    url(r"^", include(router.urls)),
    url(r'^create/$', CustomCreateView.as_view(), name='create'),
]
