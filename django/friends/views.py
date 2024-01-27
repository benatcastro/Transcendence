from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from users.models import TranscendenceUser
from users.serializers import TranscendenceUserSerializer


# Create your views here.

class TranscendenceUserFriendViewSet(ModelViewSet):
    """
    Endpoints  for Retrieving, creating and deleting friend for a user

    These endpoints requiere standard authentication
    """
    # permission_classes = [IsAuthenticated]
    serializer_class = TranscendenceUserSerializer
    queryset = TranscendenceUser.objects.all()

    def create(self, request, *args, **kwargs):
        """

        "to_user" will be  added to the "from_user" friend list and viceversa.

        Params:
            - from_user: the user that will be adding the friend
            - to_user: the user that will be added
        """

        to_user = self.request.data.get('to_user')
        from_user = self.request.data.get('from_user')
        print(from_user, "->", to_user)

        return TranscendenceUser.objects.all()
