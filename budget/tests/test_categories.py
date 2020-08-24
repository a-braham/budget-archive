from .base_tests import BaseTest
from .data import (
    CREATE_CATEGORY,
    UPDATE_CATEGORY,
    ONE_CATEGORY,
    ALL_CATEGORIES,
)


class CategoryTestCase(BaseTest):
    def test_create_catgory_user_is_anonymous(self):
        self.snapshot(
            request_string=CREATE_CATEGORY,
            variables={
                "name": "Category",
                "type": "EXPENSE",
                "description": "This is a category",
            },
        )

    def test_create_category_user_is_logged_in(self):
        self.snapshot(
            request_string=CREATE_CATEGORY,
            context={"user": self.user},
            variables={
                "name": "Category",
                "type": "EXPENSE",
                "description": "This is a category",
            },
        )

    def test_get_all_categories(self):
        self.snapshot(
            request_string=ALL_CATEGORIES, context={"user": self.user},
        )

    def test_get_category(self):
        self.snapshot(
            request_string=ONE_CATEGORY,
            context={"user": self.user},
            variables={"id": self.category.id},
        )

    def test_update_category(self):
        self.snapshot(
            request_string=UPDATE_CATEGORY,
            context={"user": self.user},
            variables={
                "id": self.category.id,
                "name": "Updated Category",
                "type": "DEBIT",
            },
        )
