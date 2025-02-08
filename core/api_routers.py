from django.urls import path, include


urlpatterns = [
    path('', include('books.api.urls')),  # 127.0.0.1:8000/api/v1/books
    path('accounts/', include('accounts.api.urls')),    # 127.0.0.1:8000/api/v1/accounts
]
