from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from cloudinary import CloudinaryImage

User = get_user_model()


class Profile(models.Model):
    """
    User profile models
    """

    user = models.OneToOneField(
        User,
        related_name="profile",
        on_delete=models.CASCADE,
    )
    phone_number = models.CharField(
        max_length=128,
        blank=True,
        null=True,
        unique=True,
    )
    first_name = models.CharField(max_length=255, blank=True)
    middle_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    image = models.ImageField(upload_to="images/", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = [
            "created_at",
        ]
        db_table = "profiles"

    def __str__(self):
        return self.user

    @property
    def get_image(self):
        """
        Property method to fetch profile image
        """
        image_url = CloudinaryImage(str(self.image)).build_url(
            width=80, height=120, crop="fill"
        )
        return image_url


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
