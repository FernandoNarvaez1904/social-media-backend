import strawberry
from django.contrib.auth import get_user_model
from strawberry.django import auto


@strawberry.django.type(get_user_model())
class User:
    username: auto
    email: auto
    email: auto
    first_name: auto
    last_name: auto
    last_login: auto
    is_active: auto


@strawberry.django.input(get_user_model())
class CreateUserInput:
    username: auto
    password: auto
    email: auto
    first_name: auto
    last_name: auto
