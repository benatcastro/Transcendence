from .models import TranscendenceUser
from rest_framework.serializers import ModelSerializer


class TranscendenceUserSerializer(ModelSerializer):
    class Meta:
        model = TranscendenceUser
        fields = ("id", "username", "email")
