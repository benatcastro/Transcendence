from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView
from intra_auth.views import FtIntraOAuth2Adapter
from django.urls import reverse
import urllib.parse
from django.shortcuts import redirect
import environ


def google_callback(request):
    env = environ.Env()
    environ.Env.read_env()
    params = urllib.parse.urlencode(request.GET)
    ip = env("IP_BACKEND")
    return redirect(f'https://{ip}/callback/google/?{params}')


def ftintra_callback(request):
    env = environ.Env()
    environ.Env.read_env()
    params = urllib.parse.urlencode(request.GET)
    ip = env("IP_BACKEND")
    response = redirect(f'https://{ip}/callback/42intra/?{params}')
    return response


class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    client_class = OAuth2Client

    @property
    def callback_url(self):
        return self.request.build_absolute_uri(reverse('google_callback'))


class FtIntraLogin(SocialLoginView):
    adapter_class = FtIntraOAuth2Adapter
    client_class = OAuth2Client

    @property
    def callback_url(self):
        return self.request.build_absolute_uri(reverse('ftintra_callback'))
