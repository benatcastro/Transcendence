from django.shortcuts import render
from rest_framework.mixins import ( CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin )
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.filters import SearchFilter
from rest_framework.exceptions import MethodNotAllowed

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

