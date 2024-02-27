from .models import MatchEntry
from rest_framework.serializers import ModelSerializer
from django.utils import timezone
from django.conf import settings

class MatchHistorySerializer(ModelSerializer):
    class Meta:
        model = MatchEntry
        fields = '__all__'
    

    # Todo use a transcendence user serializer for instance loser and winner
    def to_representation(self, instance):
        context_instance = self.context.get("instance")
        print(f"context {context_instance} -> {context_instance.id} winner {instance.winner} loser {instance.loser}")
        raw = super().to_representation(instance)
        representation = {}

        representation['date'] = raw['date']
        if context_instance == instance.winner:
            representation['oponent'] = instance.loser.username
            representation['result'] = "win"
        else:
            representation['oponent'] = instance.winner.username
            representation['result'] = "lose"

        return representation


# class MatchEntrySerializer(ModelSerializer):
#     winner = TranscendenceUserFriendSerializer()
#     loser = TranscendenceUserFriendSerializer()
    
#     class Meta:
#         model = MatchEntry
#         fields = '__all__'


