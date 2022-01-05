from typing import List

import strawberry
from django.contrib.auth import get_user_model
from strawberry.django import auto

from .filter import UserFilter


@strawberry.django.type(get_user_model())
class User:
    username: auto
    email: auto
    first_name: auto
    last_name: auto
    last_login: auto
    is_active: auto
    friends: List["User"] = strawberry.django.field(filters=UserFilter)
