# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['BudgetTestCase::test_create_budget_user_is_anonymous 1'] = {
    'data': {
        'createBudget': None
    },
    'errors': [
        {
            'locations': [
                {
                    'column': 3,
                    'line': 3
                }
            ],
            'message': 'Permission Denied!',
            'path': [
                'createBudget'
            ]
        }
    ]
}

snapshots['BudgetTestCase::test_create_budget_user_is_logged_in 1'] = {
    'data': {
        'createBudget': {
            'budget': {
                'amount': 2000.0,
                'id': '10',
                'user': {
                    'email': 'test_one@gmail.com',
                    'id': '10',
                    'username': 'test_one'
                }
            },
            'success': True
        }
    }
}

snapshots['BudgetTestCase::test_get_all_budgets 1'] = {
    'data': {
        'allBudgets': [
            {
                'amount': 10000.0,
                'id': '11'
            }
        ]
    }
}

snapshots['BudgetTestCase::test_get_budget 1'] = {
    'data': {
        'budget': {
            'amount': 10000.0,
            'id': '12'
        }
    }
}

snapshots['BudgetTestCase::test_update_budget 1'] = {
    'data': {
        'updateBudget': {
            'budget': {
                'amount': 2000.0,
                'id': '13',
                'user': {
                    'email': 'test_one@gmail.com',
                    'id': '13',
                    'username': 'test_one'
                }
            },
            'success': True
        }
    }
}
