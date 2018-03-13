from django.conf.urls import url, include
from accounts.views import FacebookLogin, GoogleLogin, CurrentUser, UpdateProfileView

urlpatterns = [

    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^facebook/$', FacebookLogin.as_view()),
    url(r'^google/$', GoogleLogin.as_view()),
    url(r'^current/$', CurrentUser.as_view()),
    url(r'^update-profile/(?P<user_id>\d+)/$', UpdateProfileView.as_view()),
]