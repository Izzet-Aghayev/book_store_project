from django.urls import path

from . import views as book_views

urlpatterns = [
    path('', book_views.ListBookViews.as_view(), name='all_books'),
    path('create/', book_views.CreateBookView.as_view(), name='create_book'),
]
