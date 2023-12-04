from allauth.socialaccount.providers.base import ProviderAccount
from allauth.socialaccount.providers.oauth2.provider import OAuth2Provider


class FtIntraAccount(ProviderAccount):
    print("gets into FtIntraAccount function")
    pass


class FtIntraOAuth2Provider(OAuth2Provider):
    id = '42intra'
    name = '42 intra auth'
    account_class = FtIntraAccount

    def extract_uid(self, data):
        """Extract uid ('user_id') and ensure it's a str."""
        return str(data["email"])

    def get_default_scope(self):
        """Ensure scope is null to fit their API."""
        return ["public"]


provider_classes = [FtIntraOAuth2Provider]
