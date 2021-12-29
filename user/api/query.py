from strawberry.django import auth
import strawberry
from .types import User


@strawberry.type
class Query:
    me: User = auth.current_user()
