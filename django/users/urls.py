from django.urls import re_path, include
from rest_framework.routers import SimpleRouter
from .views import TranscendenceUserViewSet, MeView, all_users
from django.urls import path


router = SimpleRouter()
router.register(r'', TranscendenceUserViewSet)

urlpatterns = router.urls
urlpatterns += [
    path('all', all_users),
    path('me', MeView.as_view(), name='me'),
]
