from django.contrib.auth import get_user_model

import django_filters

User = get_user_model()


class UserFilter(django_filters.FilterSet):
    class Meta:
        model = User
        fields = ["email", "username"]
