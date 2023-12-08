from django.urls import path
from .views import index, delete, search

urlpatterns = [
    path('', index, name='home'),
    path('delete', delete),
    path('search', search),
]
