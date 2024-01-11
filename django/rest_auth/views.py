from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView
from intra_auth.views import FtIntraOAuth2Adapter
from django.urls import reverse
import urllib.parse
from django.shortcuts import redirect


def google_callback(request):
    params = urllib.parse.urlencode(request.GET)

    return redirect(f'http://localhost:5173/callback/google/?{params}')


def ftintra_callback(request):
    params = urllib.parse.urlencode(request.GET)

    response = redirect(f'http://localhost:5173/callback/42intra/?{params}')

    # print("request headers: ", request.headers)
    # response['Test Header'] = 'Test Header'

    return response


class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    callback_url = 'http://localhost:5173'
    client_class = OAuth2Client

    @property
    def callback_url(self):
        return self.request.build_absolute_uri(reverse('google_callback'))


class FtIntraLogin(SocialLoginView):
    adapter_class = FtIntraOAuth2Adapter
    callback_url = 'http://example.com'
    client_class = OAuth2Client

    @property
    def callback_url(self):
        return self.request.build_absolute_uri(reverse('ftintra_callback'))
