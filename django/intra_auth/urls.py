from allauth.socialaccount.providers.oauth2.urls import default_urlpatterns

from .provider import FtIntraOAuth2Provider


urlpatterns = default_urlpatterns(FtIntraOAuth2Provider)