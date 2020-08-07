# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots["TransactionTestCase::test_create_transaction_user_is_anonymous 1"] = {
    "data": {"createTransaction": None},
    "errors": [
        {
            "locations": [{"column": 3, "line": 3}],
            "message": "Permission Denied!",
            "path": ["createTransaction"],
        }
    ],
}

snapshots["TransactionTestCase::test_create_transaction_user_is_logged_in 1"] = {
    "data": {
        "createTransaction": {
            "success": True,
            "transaction": {
                "amount": 2000.0,
                "reference": "987651234",
                "type": "DEBIT",
                "user": {
                    "email": "test_one@gmail.com",
                    "id": "10",
                    "phoneNumber": "+250780000000",
                    "username": "test_one",
                },
            },
        }
    }
}

snapshots["TransactionTestCase::test_get_all_transactions 1"] = {
    "data": {"allTransactions": [{"id": "4", "reference": "987654321"}]}
}

snapshots["TransactionTestCase::test_get_transaction 1"] = {
    "data": {
        "otherDetails": {"amount": 200.0, "type": "TEST_DEBIT"},
        "transaction": {"reference": "987654321"},
    }
}

snapshots["TransactionTestCase::test_update_transaction 1"] = {
    "data": {
        "updateTransaction": {
            "success": True,
            "transaction": {
                "amount": 2000.0,
                "reference": "987651234",
                "type": "DEBIT",
                "user": {
                    "email": "test_one@gmail.com",
                    "id": "13",
                    "phoneNumber": "+250780000000",
                    "username": "test_one",
                },
            },
        }
    }
}
