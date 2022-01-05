import strawberry_django
from django.contrib.auth import get_user_model
from strawberry_django import auto


@strawberry_django.filter(get_user_model(), lookups=True)
class UserFilter:
    username: auto
    email: auto
    first_name: auto
    last_name: auto
    last_login: auto
    is_active: auto
