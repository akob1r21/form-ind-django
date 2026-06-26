from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin



@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    search_fields = ('username',)
    

