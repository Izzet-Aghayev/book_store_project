from django.contrib import admin

from .models import (
    Category,
    Book,
    BuyBookNumber
)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_per_page = 20


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author')
    search_fields = ('title',)
    list_per_page = 20


@admin.register(BuyBookNumber)
class BuyBookNumberAdmin(admin.ModelAdmin):
    list_display = ('id', 'book', 'number')
    search_fields = ('book',)
    list_per_page = 20