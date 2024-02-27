from django.db import models
from users.models import TranscendenceUser
from django.utils import timezone

# Create your models here.
class MatchEntry(models.Model):
    winner = models.ForeignKey(TranscendenceUser, on_delete=models.CASCADE, related_name="match_won")
    loser = models.ForeignKey(TranscendenceUser, on_delete=models.CASCADE, related_name="match_lost")
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.winner} won vs {self.loser} - {self.date}'
