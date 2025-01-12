from django.contrib import admin

from .models import NewUser



@admin.register(NewUser)
class NewUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username')
    search_fields = ('username',)
    list_per_page = 25
