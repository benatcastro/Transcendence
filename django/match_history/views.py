from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet
from rest_framework.generics import ListAPIView, CreateAPIView
from .models import MatchEntry
from .serializers import MatchHistorySerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class MatchEntryViewSet(GenericViewSet, ListAPIView, CreateAPIView):
    # filter_backends = [SearchFilter]
    serializer_class = MatchHistorySerializer
    queryset = MatchEntry.objects.all()
    permission_classes = [IsAuthenticated]

    

