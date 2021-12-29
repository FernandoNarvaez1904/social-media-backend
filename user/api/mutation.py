import strawberry
from strawberry.django import auth
from .types import User, UserInput


@strawberry.type
class Mutation:
    login: User = auth.login()
    logout = auth.logout()