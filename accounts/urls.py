from django.urls import path

from . import views as accounts_views



urlpatterns = [
    path('register/', accounts_views.RegisterUserView.as_view(), name='register_user'),
    path('login/', accounts_views.RegisterUserView.as_view(), name='login'),
]
