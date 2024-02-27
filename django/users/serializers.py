from .models import TranscendenceUser
from rest_framework.serializers import ModelSerializer
from django.utils import timezone
from django.conf import settings
from match_history.serializers import MatchHistorySerializer
from match_history.models import MatchEntry
from django.db.models import Q

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
        
        
        player_matches = MatchEntry.objects.filter(Q(winner=instance) | Q(loser=instance))
        match_serializer = MatchHistorySerializer(player_matches, many=True, context={"instance": instance})
        match_history = match_serializer.data
        print("match_history: ", match_history)
        user_representation = super().to_representation(instance)

        user_representation['status'] = "online" if is_user_online(instance) else "away"
        user_representation['history'] = match_history

        return user_representation
