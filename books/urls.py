from django.urls import path

from . import views as book_views

urlpatterns = [
    path('', book_views.ListBookViews.as_view(), name='all_books'),
    path('create/', book_views.CreateBookView.as_view(), name='create_book'),
    path('detail/<int:pk>/', book_views.DetailBookView.as_view(), name='detail_book'),
    path('update/<int:pk>/', book_views.UpdateBookView.as_view(), name='update_book'),
    path('delete/<int:pk>/', book_views.DeleteBookView.as_view(), name='delete_book'),
]
