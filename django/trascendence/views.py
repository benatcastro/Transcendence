from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from django.http import JsonResponse

class HomeView(APIView):

 def get(self, request, format=None):
    return JsonResponse({"message":
    'cristian HELLO patata FROM DJANGO AND DOCKER'})

 

def index(request):
    print("¡Hola, estoy aquíiiiiii------!")
    return render(request, 'index.html')
