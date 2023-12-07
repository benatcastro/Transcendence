from django.urls import re_path, include
from rest_framework.routers import SimpleRouter
from .views import TranscendenceUserViewSet


router = SimpleRouter()
router.register(r'', TranscendenceUserViewSet)

urlpatterns = router.urls