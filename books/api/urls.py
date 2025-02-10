from django.urls import path, include


from . import views as books_views



urlpatterns = [
    path('category', books_views.ListCategoryMixinsView.as_view(), name='api_category'),

    path('detail-category/<int:pk>/', books_views.DetailCategoryMixinsView.as_view(), name='api_detail_category'),

    path('all-books', books_views.ListBookMixinsView.as_view(), name='api_all_books'),

    path('create-book/', books_views.CreateBookMixinsView.as_view(), name='api_create_book'),

    path('detail-book/<int:pk>/', books_views.DetailBookMixinsView.as_view(), name='api_detail_book'),

    path('buy/<int:pk>/', books_views.BuyBookAPIView.as_view(), name='api_buy_book'),
]
