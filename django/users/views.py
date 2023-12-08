from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.filters import SearchFilter
from rest_framework.exceptions import MethodNotAllowed
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes, permission_classes
from rest_framework.permissions import IsAuthenticated

from .models import TranscendenceUser
from .serializers import TranscendenceUserSerializer


class TranscendenceUserViewSet(ModelViewSet):
    filter_backends = [SearchFilter]
    serializer_class = TranscendenceUserSerializer
    queryset = TranscendenceUser.objects.all()
    search_fields = ["username"]
    lookup_field = 'username'

    def create(self, request, *args, **kwargs):
        raise MethodNotAllowed("POST")


from rest_framework import renderers


class CustomRenderer(renderers.JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        response_data = {'count': len(data), 'results': data}
        return super().render(response_data, accepted_media_type, renderer_context)


@api_view(['GET'])
@renderer_classes([CustomRenderer])
@permission_classes([IsAuthenticated])
def me(request):
    print("Me-> ", request.user)
    books = ['Book 1', 'Book 2', 'Book 3']
    return Response(books, status=status.HTTP_200_OK)

# class MeView(APIView):
#     def get(self, request, format=None):
#         me = [
#             {"username": "test", 'email': "test@test.com"}
#         ]
#
#         serializer = TranscendenceUserSerializer(data=me)
#         serializer.is_valid(raise_exception=True)
#         print("User in request:", request.user)
#         renderer_classes = [JSONRenderer]
#         return Response(serializer.data, status=status.HTTP_200_OK)
