from django.contrib import admin

from .models import User



@admin.register(User)
class NewUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email')
    search_fields = ('email',)
    list_per_page = 25
