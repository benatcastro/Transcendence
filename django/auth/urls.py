from django.urls import path
from . import views

urlpatterns = [
    path('42', views.ft_auth, name='index'),
]
