from .models import TranscendenceUser
from rest_framework.serializers import ModelSerializer
from django.utils import timezone
from django.conf import settings


def is_user_online(user):
    threshold = timezone.now() - timezone.timedelta(minutes=settings.USER_AWAY_THRESHOLD_MINUTES)
    try:
        return user.last_activity > threshold
    except TranscendenceUser.DoesNotExist:
        return False


class TranscendenceUserSerializer(ModelSerializer):
    class Meta:
        model = TranscendenceUser
        fields = ("id", "username", "email", "score", "pfp", "friends")

    def to_representation(self, instance):
        user_representation = super().to_representation(instance)

        # Add the status field
        user_representation['status'] = "online" if is_user_online(instance) else "away"

        return user_representation
