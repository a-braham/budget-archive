# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['AccountTestCase::test_create_account_user_is_anonymous 1'] = {
    'data': {
        'createAccount': None
    },
    'errors': [
        {
            'locations': [
                {
                    'column': 3,
                    'line': 5
                }
            ],
            'message': 'Permission Denied!',
            'path': [
                'createAccount'
            ]
        }
    ]
}

snapshots['AccountTestCase::test_create_account_user_is_logged_in 1'] = {
    'data': {
        'createAccount': {
            'account': {
                'amount': 0.0,
                'description': None,
                'institution': 'Bank',
                'name': 'Card',
                'number': 1234567890,
                'type': 'DEBIT',
                'user': {
                    'email': 'test_one@gmail.com',
                    'id': '2',
                    'username': 'test_one'
                }
            },
            'success': True
        }
    }
}

snapshots['AccountTestCase::test_get_account 1'] = {
    'data': {
        'account': {
            'name': 'TEST_CARD'
        },
        'otherDetails': {
            'amount': 0.0,
            'institution': 'TEST_BANK',
            'type': 'TEST_DEBIT'
        }
    }
}

snapshots['AccountTestCase::test_get_all_accounts 1'] = {
    'data': {
        'allAccounts': [
            {
                'id': '5',
                'name': 'TEST_CARD'
            }
        ]
    }
}

snapshots['AccountTestCase::test_update_account 1'] = {
    'data': {
        'editAccount': {
            'account': {
                'amount': 0.0,
                'description': None,
                'institution': 'Bank',
                'name': 'Card',
                'number': 1234567890,
                'type': 'DEBIT',
                'user': {
                    'email': 'test_one@gmail.com',
                    'id': '5',
                    'username': 'test_one'
                }
            },
            'success': True
        }
    }
}
