from rest_framework.routers import SimpleRouter
from .views import MatchEntryViewSet

router = SimpleRouter()
router.register(r'', MatchEntryViewSet)
urlpatterns = router.urls
