from .base_tests import BaseTest
from .data import (
    CREATE_TRANSACTION,
    UPDATE_TRANSACTION,
    ONE_TRANSACTION,
    ALL_TRANSACTIONS,
)


class TransactionTestCase(BaseTest):
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
