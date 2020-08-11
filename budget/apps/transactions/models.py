from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Transaction(models.Model):
    """
    Model class for transactions
    """

    reference = models.CharField(max_length=100, unique=True)
    type = models.CharField(max_length=100, null=False, blank=False)
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        max_length=100,
        null=False,
        blank=False,
        default=0.0,
    )
    description = models.CharField(max_length=500, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    to_account = models.IntegerField(null=False, blank=False)
    from_account = models.IntegerField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "transactions"

    def __str__(self):
        """
        Returns transaction representaion.
        """
        return self.reference
