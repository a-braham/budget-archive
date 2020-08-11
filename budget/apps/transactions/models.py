from django.db import models
from django.contrib.auth import get_user_model
from budget.apps.categories.models import Category
from budget.apps.budget.models import Budget
from budget.apps.accounts.models import Account

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
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="tr_user"
    )
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE,
        related_name="tr_category", null=True
    )
    account = models.ForeignKey(
        Account, on_delete=models.CASCADE,
        related_name="tr_account", null=True
    )
    budget = models.ForeignKey(
        Budget, on_delete=models.CASCADE, related_name="tr_budget", null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "transactions"

    def __str__(self):
        """
        Returns transaction representaion.
        """
        return self.reference
