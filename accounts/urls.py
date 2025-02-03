from django.urls import path

from . import views as accounts_views



urlpatterns = [
    path('register/', accounts_views.UserRegisterView.as_view(), name='register'),

    path('profile/', accounts_views.ProfileView.as_view(), name='profile'),

    path('login/', accounts_views.UserSignView.as_view(), name='login'),
    
    path('logout/', accounts_views.UserSignOutView.as_view(), name='logout'),

    path('delete/', accounts_views.UserDeleteView.as_view(), name='delete_user'),
]
