from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)

from django.conf import settings
from django.db import models


class UserManager(BaseUserManager):
    """
    Custom user manager
    """

    def create_user(self, email, phone_number, password=None, **extra_fields):
        """
        Create a normal user
        """
        if email is None:
            raise TypeError('User must have an email')
        if phone_number is None:
            raise TypeError('User must have a phone number')
        user = self.model(
            email=self.normalize_email(email), phone_number=phone_number, **extra_fields
        )
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, phone_number, password, **extra_fields):
        """
        create super user
        """
        if password is None:
            raise TypeError('Super user must have a passeord')

        user = self.create_user(email, phone_number, password, **extra_fields)
        user.is_superuser = True
        user.is_staff = True,
        user.is_verified = True
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """
    user model
    """
    username = models.CharField(max_length=128, db_index=True, unique=True)
    email = models.EmailField(db_index=True, unique=True)
    phone_number = models.CharField(max_length=128, blank=True, unique=True)
    first_name = models.CharField(max_length=255, blank=True)
    middle_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['phone_number']

    objects = UserManager()

    class Meta:
        db_table = "users"

    def __str__(self):
        """
        Returns user representaion.
        """
        return self.email
