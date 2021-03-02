# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['AuthTestCase::test_create_user 1'] = {
    'data': {
        'register': None
    },
    'errors': [
        {
            'locations': [
                {
                    'column': 6,
                    'line': 4
                }
            ],
            'message': '''duplicate key value violates unique constraint "profiles_phone_number_key"
DETAIL:  Key (phone_number)=() already exists.
''',
            'path': [
                'register'
            ]
        }
    ]
}
