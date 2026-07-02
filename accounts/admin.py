from django.contrib import admin
from .models import CustomUser, UserProfile
from django.contrib.auth.admin import UserAdmin



@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Extra Profile Info', {
            'fields': ('phone', 'profile_photo'),
        }),
    )




@admin.register(UserProfile)
class CustomUserAdmin(admin.ModelAdmin):
    pass    
