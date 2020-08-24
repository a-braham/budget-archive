# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['CategoryTestCase::test_create_category_user_is_logged_in 1'] = {
    'data': {
        'createCategory': {
            'category': {
                'description': 'This is a category',
                'name': 'Category',
                'type': 'EXPENSE',
                'user': {
                    'email': 'test_one@gmail.com',
                    'id': '9',
                    'phoneNumber': '+250780000001',
                    'username': 'test_one'
                }
            },
            'success': True
        }
    }
}

snapshots['CategoryTestCase::test_create_catgory_user_is_anonymous 1'] = {
    'data': {
        'createCategory': None
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
                'createCategory'
            ]
        }
    ]
}

snapshots['CategoryTestCase::test_get_all_categories 1'] = {
    'data': {
        'allCategories': [
            {
                'id': '11',
                'name': 'TEST_CATEGORY',
                'type': ''
            }
        ]
    }
}

snapshots['CategoryTestCase::test_get_category 1'] = {
    'data': {
        'category': {
            'name': 'TEST_CATEGORY',
            'type': ''
        }
    }
}

snapshots['CategoryTestCase::test_update_category 1'] = {
    'data': {
        'updateCategory': {
            'category': {
                'name': 'Updated Category',
                'type': 'DEBIT',
                'user': {
                    'email': 'test_one@gmail.com',
                    'id': '13',
                    'phoneNumber': '+250780000001',
                    'username': 'test_one'
                }
            },
            'success': True
        }
    }
}
