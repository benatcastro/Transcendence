from django.urls import path, include
from .views import GoogleLogin, FtIntraLogin

urlpatterns = [
    path('', include('dj_rest_auth.urls')),
    path('', include('allauth.urls')),
    path('registration/', include('dj_rest_auth.registration.urls')),
    path('google/', GoogleLogin.as_view(), name='google_login'),
    path('42intra/', FtIntraLogin.as_view(), name='42intra_login')
]