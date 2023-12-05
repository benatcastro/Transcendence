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
        return str(data["id"])

    def get_default_scope(self):
        """Ensure scope is null to fit their API."""
        return ["public"]

    def extract_common_fields(self, data):
        print("===EXTRACT COMMON FIELDS===")

        return dict(
            email= data.get("email"),
            username=data.get("login"),
        )


provider_classes = [FtIntraOAuth2Provider]
