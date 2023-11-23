from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from django.http import JsonResponse

class HomeView(APIView):
 
 def get(self, request, format=None):
    return JsonResponse({"message":
    'HELLO WORLD FROM DJANGO AND DOCKER'})
