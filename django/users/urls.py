from django.urls import re_path, include
from rest_framework.routers import SimpleRouter
from .views import TranscendenceUserViewSet, me
from django.urls import path


router = SimpleRouter()
router.register(r'', TranscendenceUserViewSet)

urlpatterns = router.urls

urlpatterns += [
    path('me', me, name="me"),
]