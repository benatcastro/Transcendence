from .views import TranscendenceUserFriendViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r'', TranscendenceUserFriendViewSet)
urlpatterns = router.urls
