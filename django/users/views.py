from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.filters import SearchFilter
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.shortcuts import get_object_or_404

from .models import TranscendenceUser
from .serializers import TranscendenceUserSerializer

class TranscendenceUserViewSet(ModelViewSet):
    """
.   View class-set for all the user handling endpoints.
    Post is not allowed since the user creation is done via authentication workflow.
    More info at https://www.django-rest-framework.org/api-guide/viewsets/#modelviewset

    Attributes:
        - serializer_class: class used to serialize the model.
        - queryset: user data where the querys will be applied.
        - permssion_classes: the request will be authenticad with DRF IsAuthenticated method.
        - search_fields: when the request contains the search query users will be searched using this fields.
        - lookup_fields: the field used to lookup for the user.

    Methods:
        - get_allowed_metohds(): override, disallowing the post method to this endpoint
    """
    filter_backends = [SearchFilter]
    serializer_class = TranscendenceUserSerializer
    queryset = TranscendenceUser.objects.all()
    search_fields = ["username"]
    lookup_field = 'username'
    permission_classes = [IsAuthenticated]

    def get_allowed_methods(self):
        methods = super().get_allowed_methods()
        methods.remove('POST')
        return methods

class MeView(RetrieveAPIView):
    """
     /users/me endpoint hoandling
     Returns the authenticated user data
     This api vew inherits RetrieveApiView, so it's a read-only one object return view
    Attributes:
        - serializer_class: class used to serialize the model.
        - permssion_classes: the request will be authenticad with DRF IsAuthenticated method.
    Methods:
        - get_queryset(): override, returns the dataset of the users, a filter is applied where the email is the same as
                          the requester.
        - get_object(): returns the currently authenticated user

    """
    queryset = TranscendenceUser.objects.all()
    serializer_class = TranscendenceUserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        obj = get_object_or_404(self.queryset, email=self.request.user.email)
        print("\n\n", obj, "\n\n")
        return obj

@api_view(['GET'])
@permission_classes([AllowAny])
def all_users(request):
    users = TranscendenceUser.objects.all()
    serializer = TranscendenceUserSerializer(users, many=True)
    return Response(serializer.data)
