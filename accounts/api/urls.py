from django.urls import path

from . import views as accounts_views



urlpatterns = [
    path('api_register', accounts_views.RegisterAPIView.as_view(), name='api_register'),
    path('api_login', accounts_views.LoginAPIView.as_view(), name='api_login'),
    path('api_logout', accounts_views.LogoutAPIView.as_view(), name='api_logout'),
    path('api_delete', accounts_views.DeleteUserAPIView.as_view(), name='api_delete'),
    path('api_profile', accounts_views.ProfileUserAPIView.as_view(), name='api_profile'),
]