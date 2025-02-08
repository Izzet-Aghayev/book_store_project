from django.urls import path, include


from . import views as books_views



urlpatterns = [
    path('api_category', books_views.CategoryMixinsView.as_view(), name='api_category'),
    path('api_category/<int:pk>/', books_views.CategoryDetailMixinsView.as_view(), name='api_detail_category'),
]
