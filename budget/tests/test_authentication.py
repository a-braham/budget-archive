from django.contrib.auth import get_user_model

from .base_tests import BaseTest
from .data import CREATE_USER

User = get_user_model()


class AuthTestCase(BaseTest):
    def setUp(self):
        super().setUp()

        self.user = User.objects.create(
            username="test_one",
            email="test_one@gmail.com",
            phone_number="+250780000001",
            password="test#pa55",
        )

    def test_create_user(self):
        self.snapshot(
            request_string=CREATE_USER,
            variables={
                "email": "test_user@budget.com",
                "username": "test_user",
                "phone_number": "+250780000000",
                "first_name": "Test",
                "last_name": "User",
                "password": "te5tPa$$",
            },
        )

    def test_create_model_user(self):  # no snapshot
        """
          A model test method for creating users
          """
        self.assertIsInstance(self.user, User)
