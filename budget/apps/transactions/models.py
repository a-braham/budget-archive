from django.db import models
from django.contrib.auth import get_user_model
from budget.apps.accounts.models import Account
from budget.apps.budget.models import Budget

User = get_user_model()

class Transaction(models.Model):
  """
  Model class for transactions
  """
  amount = models.DecimalField(max_digits=None, max_length=100, default=0.0)
  description = models.CharField(max_length=500, null=True, blank=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transaction_user')
  account = models.ForeignKey(Transaction, on_delete=models.CASCADE, related_name='transaction_account')
  budget = models.ForeignKey(Budget, on_delete=models.CASCADE, related_name='transaction_budget')
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  class Meta:
    db_table = 'transactions'

  def __str__(self):
        """
        Returns transaction representaion.
        """
        return self.name
