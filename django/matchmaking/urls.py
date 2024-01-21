from django.urls import path
from .views import show, delete, clear, search, create
urlpatterns = [
    path('', show),
    path('create-usr', create),
    path('delete', delete),
    path('clear', clear),
    path('search', search),
]