from django.db.models.signals  import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import UserProfile

User = get_user_model()

@receiver(post_save, sender=User)
def create_profile(sender, created, instance,   **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
        print('for this user has been created profile using signals', instance.username)
    else:
        print(f'{instance.username} was updated')
        print(kwargs)
    

@receiver(post_delete, sender=User)
def delete_image(sender, instance, **kwargs):
    if instance.profile_photo:
        instance.profile_photo.delete(save=False)