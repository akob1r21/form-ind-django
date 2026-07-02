from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    profile_photo = models.ImageField(upload_to='users/', null=True, blank=True)
    phone = models.CharField(max_length=13, null=True, blank=True)

    def __str__(self):
        return self.username
    


class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.user.username
    