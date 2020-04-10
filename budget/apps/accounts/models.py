from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Account(models.Model):
    """
    Model class for accounts
    """
    name = models.CharField(
        max_length=100, null=False,
        blank=False, default='card'
    )
    type = models.CharField(
        max_length=100, null=False,
        blank=False, default='regular'
    )
    institution = models.CharField(
        max_length=255, null=False, blank=False
    )
    description = models.CharField(max_length=500, null=True, blank=True)
    amount = models.DecimalField(
        max_digits=10, decimal_places=2, max_length=100, default=0.0)
    number = models.BigIntegerField(blank=True, null=True, unique=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='account_user')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'accounts'

    def __str__(self):
        """
        Returns account representaion.
        """
        return self.name
