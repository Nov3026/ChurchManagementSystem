from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from custom_user.models import CustomUser
from .models import Member


@receiver(post_save, sender=CustomUser)
def create_member_profile(sender, instance, created, **kwargs):
    if created:
        Member.objects.create(
            user=instance,
            first_name=instance.first_name,
            last_name=instance.last_name,
            email=instance.email,
        )


@receiver(post_save, sender=CustomUser)
def save_member_profile(sender, instance, **kwargs):
    try:
        profile = instance.member_user  # Access Member using the related_name
        # Update only fields that are blank or need synchronization
        if not profile.first_name:
            profile.first_name = instance.first_name
        if not profile.last_name:
            profile.last_name = instance.last_name
        if not profile.email:
            profile.email = instance.email
        profile.save()
    except Member.DoesNotExist:
        Member.objects.create(
            user=instance,
            first_name=instance.first_name,
            last_name=instance.last_name,
            email=instance.email,
        )


@receiver(post_delete, sender=Member)
def delete_user(sender, instance, **kwargs):
     """
    Deletes the associated User when a UserProfile is deleted.
    """
     if instance.user:
         instance.user.delete()
         