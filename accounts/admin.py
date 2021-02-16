from django.contrib import admin
from .models import Profile
# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'user_name']
    list_display_links = ['user', 'user_name']
    search_fields = ['user_name']