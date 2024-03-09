from users.models import TranscendenceUser
from users.serializers import TranscendenceUserSerializer
from rest_framework.serializers import ModelSerializer


class TranscendenceUserFriendSerializer(ModelSerializer):
    friends = TranscendenceUserSerializer(many=True, read_only=True)

    class Meta:
        model = TranscendenceUser
        fields = ("id", "username", "friends", "pfp")