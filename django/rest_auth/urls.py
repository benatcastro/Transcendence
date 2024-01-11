from django.urls import path, include
from .views import GoogleLogin, FtIntraLogin, google_callback, ftintra_callback
from allauth.socialaccount.providers.google import views as google_views
from intra_auth import views as intra_views

urlpatterns = [

    path('', include('dj_rest_auth.urls')),
    # Google api endpoints
    path('google/', GoogleLogin.as_view(), name='google_login'),
    path('google/login/callback/', google_callback, name="google_callback"),
    path('google/login/', google_views.oauth2_login),

    # Intra api endpoints
    path('42intra/', FtIntraLogin.as_view(), name='ftintra_login'),
    path('42intra/login/callback/', ftintra_callback, name="ftintra_callback"),
    path('42intra/login/', intra_views.oauth2_login),

    # General auth endpoints
    path('', include('allauth.urls')),
    path('', include('intra_auth.urls')),
]