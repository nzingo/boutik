from django.db import models
from django.contrib.auth.models import AbstractUser
from allauth.account.signals import user_signed_up
from django.dispatch import receiver


class CustomUser(AbstractUser):

    image_url = models.CharField(max_length=200, blank=True)
    description = models.TextField(default='', blank=True)
    user_name = models.CharField(max_length=100, default='', blank=True)
    first_name = models.CharField(max_length=50, default='', blank=True)
    last_name = models.CharField(max_length=50, default='', blank=True)
    gender = models.CharField(max_length=20, default='', blank=True)
    city = models.CharField(max_length=50, default='', blank=True)
    phone_number = models.CharField(max_length=20, default='', blank=True)
    date_of_birth = models.DateField(null=True, blank=True)

    USERNAME_FIELD = 'username'



@receiver(user_signed_up)
def init_account(sociallogin, user, **kwargs):

    user.user_name = user.first_name + " " + user.last_name

    if sociallogin.account.provider == 'facebook':
        social_id = sociallogin.account.extra_data['id']
        user.image_url = 'https://graph.facebook.com/' + social_id + '/picture?type=square&height=600&width=600&return_ssl_resources=1'

    if sociallogin.account.provider == 'google':
        user.image_url = sociallogin.account.extra_data['picture']

    user.save()
