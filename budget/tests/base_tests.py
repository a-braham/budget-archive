from django.contrib.auth.models import AnonymousUser
from django.test import RequestFactory
from django.contrib.auth import get_user_model
from snapshottest.django import TestCase
from graphene.test import Client

from budget.schema import schema
from budget.apps.accounts.models import Account
from budget.apps.categories.models import Category
from budget.apps.transactions.models import Transaction

User = get_user_model()

class BaseTest(TestCase):
    """
    Class to set up test case
    """

    def setUp(self):
        super().setUp()
        self.client = Client(schema)

        self.user = User.objects.create(
            username="test_one",
            email="test_one@gmail.com",
            phone_number="+250780000001",
            password="test#pa55",
        )

        self.account = Account.objects.create(
            name='TEST_CARD',
            institution='TEST_BANK',
            type='TEST_DEBIT',
            number='987654321',
            user=self.user
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

    def snapshot(self, request_string, context=None, variables=None):
        if context is None:
            context = {}
        if variables is None:
            variables = {}
        graphql_response = self.client.execute(
            request_string,
            variables=variables,
            context=self.generate_context(**context)
        )
        self.assertMatchSnapshot(graphql_response)

    def generate_context(self, user=None, files=None):
        request = RequestFactory()
        context_value = request.get('/graphql/')
        context_value.user = user or AnonymousUser()
        self.__set_context_files(context_value, files)
        return context_value

    @staticmethod
    def __set_context_files(context, files):
        if isinstance(files, dict):
            for name, file in files.items():
                context.FILES[name] = file
