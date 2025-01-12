from django.urls import path

from . import views as accounts_views



urlpatterns = [
    path('register/', accounts_views.UserRegisterView.as_view(), name='register'),
    path('login/', accounts_views.UserSignView.as_view(), name='login'),
]
