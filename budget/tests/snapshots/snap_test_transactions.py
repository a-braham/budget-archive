# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TransactionTestCase::test_create_transaction_expense 1'] = {
    'data': {
        'createTransaction': {
            'success': True,
            'transaction': {
                'amount': 2000.0,
                'reference': '987651236',
                'type': 'EXPENSE',
                'user': {
                    'email': 'test_one@gmail.com',
                    'id': '19',
                    'username': 'test_one'
                }
            }
        }
    }
}

snapshots['TransactionTestCase::test_create_transaction_income 1'] = {
    'data': {
        'createTransaction': {
            'success': True,
            'transaction': {
                'amount': 2000.0,
                'reference': '987651235',
                'type': 'INCOME',
                'user': {
                    'email': 'test_one@gmail.com',
                    'id': '20',
                    'username': 'test_one'
                }
            }
        }
    }
}

snapshots['TransactionTestCase::test_create_transaction_user_is_anonymous 1'] = {
    'data': {
        'createTransaction': None
    },
    'errors': [
        {
            'locations': [
                {
                    'column': 3,
                    'line': 6
                }
            ],
            'message': 'Permission Denied!',
            'path': [
                'createTransaction'
            ]
        }
    ]
}

snapshots['TransactionTestCase::test_create_transaction_user_is_logged_in 1'] = {
    'data': {
        'createTransaction': {
            'success': True,
            'transaction': {
                'amount': 2000.0,
                'reference': '987651234',
                'type': 'TRANSFER',
                'user': {
                    'email': 'test_one@gmail.com',
                    'id': '22',
                    'username': 'test_one'
                }
            }
        }
    }
}

snapshots['TransactionTestCase::test_get_all_transactions 1'] = {
    'data': {
        'allTransactions': [
            {
                'id': '25',
                'reference': '987654321'
            }
        ]
    }
}

snapshots['TransactionTestCase::test_get_transaction 1'] = {
    'data': {
        'otherDetails': {
            'amount': 200.0,
            'type': 'TEST_DEBIT'
        },
        'transaction': {
            'reference': '987654321'
        }
    }
}

snapshots['TransactionTestCase::test_update_transaction 1'] = {
    'data': {
        'updateTransaction': {
            'success': True,
            'transaction': {
                'amount': 2000.0,
                'reference': '987651234',
                'type': 'EXPENSE',
                'user': {
                    'email': 'test_one@gmail.com',
                    'id': '25',
                    'username': 'test_one'
                }
            }
        }
    }
}
