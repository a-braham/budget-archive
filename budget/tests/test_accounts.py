from django.contrib.auth import get_user_model
from .base_tests import BaseTest


CREATE_MUTATION = """
mutation CreateAccount($name: String!, $institution: String!, $type: String!, $number: String!){
  createAccount(name: $name, institution: $institution, type: $type, number: $number){
    success
    account {
      name,
      institution,
      type,
      amount,
      number,
      description,
      createdAt,
      user {
        id,
        username,
        email,
        phoneNumber
      }
    }
  }
}
"""

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

    def test_create_account_user_is_anonymous(self):  # snapshot
        self.snapshot(request_string=CREATE_MUTATION,
                      variables={
                          'name': 'Card',
                          'institution': 'Bank',
                          'type': 'DEBIT',
                          'number': '1234567890'
                      })

    def test_create_account_user_is_logged_in(self):  # snapshot
        self.snapshot(request_string=CREATE_MUTATION,
                      context={'user': self.user},
                      variables={
                          'name': 'Card',
                          'institution': 'Bank',
                          'type': 'DEBIT',
                          'number': '1234567890'
                      })

