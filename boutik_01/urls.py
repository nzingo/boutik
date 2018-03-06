from django.contrib import admin
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^register/', include('accounts.urls')),
    url(r'^items/', include('items.urls')),
]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)