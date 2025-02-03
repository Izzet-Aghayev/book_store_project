from django.contrib import admin

from .models import (
    User, 
    Profile,
)



@admin.register(User)
class NewUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email')
    search_fields = ('email',)
    list_per_page = 25


@admin.register(Profile)
class NewUserAdmin(admin.ModelAdmin):
    readonly_fields = ('email',)
    list_display = ('id', 'user')
    search_fields = ('user',)
    list_per_page = 25
