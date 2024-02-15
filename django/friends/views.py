from rest_framework.viewsets import GenericViewSet
from users.models import TranscendenceUser
from .serializers import TranscendenceUserFriendSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.mixins import RetrieveModelMixin, DestroyModelMixin

# Create your views here.

class TranscendenceUserFriendViewSet(GenericViewSet, RetrieveModelMixin, DestroyModelMixin):
    """
    Endpoints  for Retrieving, creating and deleting friend for a user

    These endpoints requiere standard authentication
    """
    permission_classes = [IsAuthenticated]
    lookup_field = 'username'
    serializer_class = TranscendenceUserFriendSerializer
    queryset = TranscendenceUser.objects.all()

    def create(self, request, *args, **kwargs):
        """
        param1 --  from_user: the user that will be adding the friend
        param2 -- to_user: the user that will be added

        "to_user" will be  added to the "from_user" friend list and viceversa.
        ---
        parameters:
            - name: name
              description: Foobar long description goes here
              required: true
              type: string
              paramType: form
        """

        to_user = get_object_or_404(TranscendenceUser, username=self.request.data.get('to_user'))
        from_user = get_object_or_404(TranscendenceUser, username=self.request.data.get('from_user'))

        if to_user == from_user:
            return Response(data={'message': "Error: from user and to_user are the same"},
                            status=status.HTTP_400_BAD_REQUEST)

        to_user.friends.add(from_user)
        serializer = self.get_serializer(from_user)

        return Response(data={'message': f'{from_user} and {to_user} friendship added succesfully', "update": serializer.data}, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        """
            "to_user" will be deleted from the "from_user" friend list and viceversa.
        """

        to_user = get_object_or_404(TranscendenceUser, username=self.request.data.get('to_user'))
        from_user = get_object_or_404(TranscendenceUser, username=self.kwargs.get(self.lookup_field))
        print("from user in deleting: ", from_user)
        if to_user == from_user:
            return Response(data={'message': "Error: from user and to_user are the same"},
                            status=status.HTTP_400_BAD_REQUEST)

        from_user.friends.remove(to_user)
        serializer = self.get_serializer(from_user)

        return Response(data={'message': f'{from_user} and {to_user} friendship deleted successfully',
                        "update": serializer.data},
                        status=status.HTTP_200_OK)
