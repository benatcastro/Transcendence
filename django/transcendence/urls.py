from django.urls import path, include
from .views import index
from . import views

from .views import DataUsersViewSet
from rest_framework.routers import DefaultRouter

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Andy String API",
        default_version='v1',
        description="goodbye c practice",
        terms_of_service="https://www.youtube.com/watch?v=8YCCauW8m0o",
        contact=openapi.Contact(email="cbustama@student.42urduliz.com"),
        license=openapi.License(name="Andy License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = DefaultRouter()
router.register(r'users', DataUsersViewSet, basename='user')



urlpatterns = [
    path('home', index, name='home'),
    path('', views.getData, name='getData'),
    path('api/', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
