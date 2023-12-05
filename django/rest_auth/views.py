from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView
from intra_auth.views import FtIntraOAuth2Adapter


class GoogleLogin(SocialLoginView):  # if you want to use Authorization Code Grant, use this
    adapter_class = GoogleOAuth2Adapter
    callback_url = 'http://localhost:8000/accounts/google/login/callback'
    client_class = OAuth2Client


class FtIntraLogin(SocialLoginView):
    adapter_class = FtIntraOAuth2Adapter
    callback_url = 'http://example.com'
    client_class = OAuth2Client
