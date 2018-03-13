from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from rest_auth.registration.views import SocialLoginView
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response

from accounts.models import CustomUser
from accounts.serializers import UserSerializerUpdate


class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter


class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter


class CurrentUser(APIView):
    @staticmethod
    def get(request):
        user = request.user
        print(user.username)
        return Response(user.username)


class UpdateProfileView(APIView):
    """
    update profile
    """

    @staticmethod
    def patch(request, user_id):
        user = request.user
        serializer = UserSerializerUpdate(user, data=request.data, context={'request': request}, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response('successful')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
