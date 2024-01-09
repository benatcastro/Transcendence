from rest_framework import serializers
from users.models import TranscendenceUser

class DataUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = TranscendenceUser
        fields = '__all__'
