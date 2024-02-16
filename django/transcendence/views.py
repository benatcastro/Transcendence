from django.shortcuts import render, redirect
from django.db import connection
from users.models import  TranscendenceUser
from django.http import JsonResponse
from faker import Faker
from django.http import HttpResponse
# views.py
from django.db import IntegrityError

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .serializers import DataUsersSerializer  # Asegúrate de que el nombre sea correcto


# views.py


from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .serializers import DataUsersSerializer  # Asegúrate de que el nombre sea correcto


class DataUsersViewSet(viewsets.ModelViewSet):
    queryset = TranscendenceUser.objects.all()
    serializer_class = DataUsersSerializer

def getData(request):
    # Obtener información sobre la tabla
    with connection.cursor() as cursor_info:
        cursor_info.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'")
        tablas = [fila[0] for fila in cursor_info.fetchall()]

    # Obtener contenido de la tabla
    resultados = []
    for tabla in tablas:
        with connection.cursor() as cursor_data:
            cursor_data.execute(f"SELECT * FROM {tabla}")
            contenido_tabla = [dict(zip([desc[0] for desc in cursor_data.description], fila)) for fila in cursor_data.fetchall()]
            resultados.append({'nombre_tabla': tabla, 'contenido_tabla': contenido_tabla})

    # Si la solicitud incluye 'application/json', devuelve una respuesta JSON
    if request.headers.get('Accept') == 'application/json':
        return JsonResponse({'tablas': resultados})

    # Si no, renderiza una plantilla HTML
    context = {'tablas': resultados}
    return render(request, 'index.html', context)

    

# Create your views here.

def index(request):
    return render(request, 'index.html')



class DataUsersViewSet(viewsets.ModelViewSet):
    queryset = TranscendenceUser.objects.all()
    serializer_class = DataUsersSerializer

def getData(request):
    # Obtener información sobre la tabla
    with connection.cursor() as cursor_info:
        cursor_info.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'")
        tablas = [fila[0] for fila in cursor_info.fetchall()]

    # Obtener contenido de la tabla
    resultados = []
    for tabla in tablas:
        with connection.cursor() as cursor_data:
            cursor_data.execute(f"SELECT * FROM {tabla}")
            contenido_tabla = [dict(zip([desc[0] for desc in cursor_data.description], fila)) for fila in cursor_data.fetchall()]
            resultados.append({'nombre_tabla': tabla, 'contenido_tabla': contenido_tabla})

    # Si la solicitud incluye 'application/json', devuelve una respuesta JSON
    if request.headers.get('Accept') == 'application/json':
        return JsonResponse({'tablas': resultados})

    # Si no, renderiza una plantilla HTML
    context = {'tablas': resultados}
    return render(request, 'index.html', context)

    

# Create your views here.

def index(request):
    return render(request, 'index.html')

fake = Faker()
def create_users(request):
    nombres = ["Andy String el Mas guapo", "Ander Maestro de los Maestro", "bcastro", "Angeru PiedPiper", "Toñooo God DevOps", "hola, soy un gato"]

    for nombre in nombres:
        correo = fake.email()
        contraseña = fake.password()
        try:
            TranscendenceUser.objects.create(
                password=contraseña,
                email=correo,
                username=nombre,
                creation_method="RE"
            )
        except IntegrityError as e:
            pass

    return redirect('getData')