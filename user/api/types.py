from typing import List

import strawberry
import strawberry_django
from django.contrib.auth import get_user_model
from strawberry.django import auto


@strawberry_django.filter(get_user_model(), lookups=True)
class UserFilter:
    username: auto
    email: auto
    first_name: auto
    last_name: auto
    last_login: auto
    is_active: auto


@strawberry.django.type(get_user_model())
class User:
    username: auto
    email: auto
    first_name: auto
    last_name: auto
    last_login: auto
    is_active: auto
    friends: List["User"] = strawberry.django.field(filters=UserFilter)


@strawberry.django.input(get_user_model())
class CreateUserInput:
    username: auto
    password: auto
    email: auto
    first_name: auto
    last_name: auto


@strawberry_django.input(get_user_model())
class DeleteUserInput:
    password: auto
