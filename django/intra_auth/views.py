import requests

from allauth.socialaccount.providers.oauth2.views import (
    OAuth2Adapter,
    OAuth2CallbackView,
    OAuth2LoginView,
)

from .provider import FtIntraOAuth2Provider


class FtIntraOAuth2Adapter(OAuth2Adapter):
    provider_id = FtIntraOAuth2Provider.id

    authorize_url = 'https://api.intra.42.fr/oauth/authorize'
    access_token_url = 'https://api.intra.42.fr/oauth/token'
    profile_url = 'https://api.intra.42.fr/v2/me'

    def complete_login(self, request, app, token, **kwargs):
        """Complete login, ensuring correct OAuth header."""
        headers = {"Authorization": "Bearer {0}".format(token.token)}
        metadata = requests.get(self.profile_url, headers=headers)
        print('profile status:', metadata.status_code)
        extra_data = metadata.json()
        # print("complete_login:", extra_data)
        return self.get_provider().sociallogin_from_response(request, extra_data)


oauth2_login = OAuth2LoginView.adapter_view(FtIntraOAuth2Adapter)
oauth2_callback = OAuth2CallbackView.adapter_view(FtIntraOAuth2Adapter)