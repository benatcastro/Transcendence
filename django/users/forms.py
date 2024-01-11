from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import TranscendenceUser


class TranscendenceUserCreationForm(UserCreationForm):

    class Meta:
        model = TranscendenceUser
        fields = ("email",)


class TranscendenceUserChangeForm(UserChangeForm):

    class Meta:
        model = TranscendenceUser
        fields = ("email",)
