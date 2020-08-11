from django.contrib.auth import get_user_model

from .base_tests import BaseTest
from .data import (
    CREATE_TRANSACTION,
    UPDATE_TRANSACTION,
    ONE_TRANSACTION,
    ALL_TRANSACTIONS,
)
from budget.apps.transactions.models import Transaction
from budget.apps.accounts.models import Account
from budget.apps.categories.models import Category

User = get_user_model()


class TransactionTestCase(BaseTest):
    def setUp(self):
        super().setUp()
        self.user = User.objects.create(
            username="test_one",
            email="test_one@gmail.com",
            phone_number="+250780000000",
            password="test#pa55",
        )

        self.account = Account.objects.create(
            name="TEST_CARD",
            institution="TEST_BANK",
            type="TEST_DEBIT",
            number="987654321",
            user=self.user,
        )

        self.category = Category.objects.create(
            name="TEST_CATEGORY", user=self.user
        )

        self.transaction = Transaction.objects.create(
            reference="987654321",
            type="TEST_DEBIT",
            amount="200.0",
            user=self.user,
            to_account=self.account.id,
            from_account=self.account.id,
        )

    def test_create_transaction_user_is_anonymous(self):
        self.snapshot(
            request_string=CREATE_TRANSACTION,
            variables={
                "reference": "987651234",
                "type": "TRANSFER",
                "amount": "2000.0",
                "from_account": self.account.id,
                "to_account": self.account.id,
            },
        )

    def test_create_transaction_user_is_logged_in(self):
        self.snapshot(
            request_string=CREATE_TRANSACTION,
            context={"user": self.user},
            variables={
                "reference": "987651234",
                "type": "TRANSFER",
                "amount": "2000.0",
                "from_account": self.account.id,
                "to_account": self.account.id,
            },
        )

    def test_create_transaction_income(self):
        self.snapshot(
            request_string=CREATE_TRANSACTION,
            context={"user": self.user},
            variables={
                "reference": "987651235",
                "type": "INCOME",
                "amount": "2000.0",
                "from_account": self.category.id,
                "to_account": self.account.id,
            },
        )

    def test_create_transaction_expense(self):
        self.snapshot(
            request_string=CREATE_TRANSACTION,
            context={"user": self.user},
            variables={
                "reference": "987651236",
                "type": "EXPENSE",
                "amount": "2000.0",
                "from_account": self.account.id,
                "to_account": self.category.id,
            },
        )

    def test_get_all_transactions(self):
        context = {"user": self.user}
        self.snapshot(request_string=ALL_TRANSACTIONS, context=context)

    def test_get_transaction(self):
        self.snapshot(
            request_string=ONE_TRANSACTION,
            context={"user": self.user},
            variables={
                "id": self.transaction.id,
                "reference": self.transaction.reference,
            },
        )

    def test_update_transaction(self):
        self.snapshot(
            request_string=UPDATE_TRANSACTION,
            context={"user": self.user},
            variables={
                "id": self.transaction.id,
                "reference": "987651234",
                "type": "EXPENSE",
                "amount": "2000.0",
            },
        )
