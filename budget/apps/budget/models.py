from django.db import models
from django.contrib.auth import get_user_model

from budget.apps.categories.models import Category

User = get_user_model()


class Budget(models.Model):
    """
  Model class for budget
  """

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(
        max_digits=10, decimal_places=2, max_length=100, default=0.0
    )
    description = models.CharField(max_length=500, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "budgets"

    def __str__(self):
        """
        Returns budget representaion.
        """
        return self.name
