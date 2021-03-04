# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['AuthTestCase::test_create_user 1'] = {
    'errors': [
        {
            'locations': [
                {
                    'column': 7,
                    'line': 13
                }
            ],
            'message': 'Cannot query field "isVerified" on type "UserType".'
        }
    ]
}
