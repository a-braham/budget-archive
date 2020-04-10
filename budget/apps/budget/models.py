from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Budget(models.Model):
  """
  Model class for budget
  """
  name = models.CharField(max_length=255, null=False, blank=False, unique=True)
  description = models.CharField(max_length=500, null=True, blank=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='budget_user')
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  class Meta:
    db_table = 'budgets'

  def __str__(self):
        """
        Returns budget representaion.
        """
        return self.name
