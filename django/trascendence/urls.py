from django.urls import path
from .views import HomeView, index

urlpatterns = [
    path('', index, name='index'),
    path('home/', HomeView.as_view(), name='home'),
]
