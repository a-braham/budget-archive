from django.contrib.auth import get_user_model

from .base_tests import BaseTest
from .data import (
    CREATE_MUTATION, UPDATE_MUTATION, ONE_ACCOUNT, ALL_ACCOUNTS
)
from budget.apps.accounts.models import Account

User = get_user_model()


class AccountTestCase(BaseTest):
    def setUp(self):
        super().setUp()
        self.user = User.objects.create(
            username='test_one',
            email='test_one@gmail.com',
            phone_number='+250780000000',
            password='test#pa55'
        )

        self.account = Account.objects.create(
            name='TEST_CARD',
            institution='TEST_BANK',
            type='TEST_DEBIT',
            number='987654321',
            user=self.user
        )

    def test_create_account_user_is_anonymous(self):
        self.snapshot(request_string=CREATE_MUTATION,
                      variables={
                          'name': 'Card',
                          'institution': 'Bank',
                          'type': 'DEBIT',
                          'number': '1234567890'
                      })

    def test_create_account_user_is_logged_in(self):
        self.snapshot(request_string=CREATE_MUTATION,
                      context={'user': self.user},
                      variables={
                          'name': 'Card',
                          'institution': 'Bank',
                          'type': 'DEBIT',
                          'number': '1234567890'
                      })

    def test_get_all_accounts(self):
        self.snapshot(request_string=ALL_ACCOUNTS, context={'user': self.user})

    def test_get_account(self):
      self.snapshot(request_string=ONE_ACCOUNT,
                      context={'user': self.user},
                      variables={
                          'id': self.account.id,
                          'number': self.account.number,
                      })

    def test_update_account(self):
        self.snapshot(request_string=UPDATE_MUTATION,
                      context={'user': self.user},
                      variables={
                          'id': self.account.id,
                          'name': 'Card',
                          'institution': 'Bank',
                          'type': 'DEBIT',
                          'number': '1234567890'
                      })
