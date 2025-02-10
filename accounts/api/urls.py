from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

from django.urls import path

from . import views as accounts_views



urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    path('api-register', accounts_views.RegisterAPIView.as_view(), name='api_register'),
    path('api-login', accounts_views.LoginAPIView.as_view(), name='api_login'),
    path('api-logout', accounts_views.LogoutAPIView.as_view(), name='api_logout'),
    path('api-delete', accounts_views.DeleteUserAPIView.as_view(), name='api_delete'),
    path('api-profile', accounts_views.ProfileUserAPIView.as_view(), name='api_profile'),
]