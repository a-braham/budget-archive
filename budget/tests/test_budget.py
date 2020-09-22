from .base_tests import BaseTest
from .data import (
    CREATE_BUDGET,
    UPDATE_BUDGET,
    ONE_BUDGET,
    ALL_BUDGETS,
)


class BudgetTestCase(BaseTest):
    def test_create_budget_user_is_anonymous(self):
        self.snapshot(
            request_string=CREATE_BUDGET,
            variables={"amount": "2000.0", "category": self.category.id},
        )

    def test_create_budget_user_is_logged_in(self):
        self.snapshot(
            request_string=CREATE_BUDGET,
            context={"user": self.user},
            variables={"amount": "2000.0", "category": self.category.id},
        )

    def test_get_all_budgets(self):
        context = {"user": self.user}
        self.snapshot(request_string=ALL_BUDGETS, context=context)

    def test_get_budget(self):
        self.snapshot(
            request_string=ONE_BUDGET,
            context={"user": self.user},
            variables={"id": self.budget.id},
        )

    def test_update_budget(self):
        self.snapshot(
            request_string=UPDATE_BUDGET,
            context={"user": self.user},
            variables={"id": self.budget.id, "amount": "2000.0"},
        )
