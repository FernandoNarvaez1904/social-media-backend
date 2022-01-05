import strawberry_django
from django.contrib.auth import get_user_model
from strawberry_django import auto


@strawberry_django.input(get_user_model())
class CreateUserInput:
    username: auto
    password: auto
    email: auto
    first_name: auto
    last_name: auto


@strawberry_django.input(get_user_model())
class DeleteUserInput:
    password: auto
