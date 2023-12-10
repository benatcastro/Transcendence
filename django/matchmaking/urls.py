from django.urls import path
from .views import index, delete, deleteAll, search

urlpatterns = [
    path('', index, name='home'),
    path('delete', delete),
    path('deleteAll', deleteAll),
    path('search', search),
]
