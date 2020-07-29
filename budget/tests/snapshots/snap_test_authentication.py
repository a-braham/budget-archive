# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots["AuthTestCase::test_create_user 1"] = {
    "data": {
        "register": {
            "user": {
                "email": "test_user@budget.com",
                "firstName": "Test",
                "isActive": False,
                "isVerified": False,
                "lastName": "User",
                "middleName": "",
                "phoneNumber": "+250780000000",
                "username": "test_user",
            }
        }
    }
}
