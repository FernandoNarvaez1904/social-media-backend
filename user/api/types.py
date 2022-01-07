from typing import List

import strawberry
from django.contrib.auth import get_user_model
from strawberry.django import auto

from .filter import UserFilter
from ..models import FriendRequest


@strawberry.django.type(get_user_model())
class UserType:
    id: strawberry.scalars.ID
    username: auto
    email: auto
    first_name: auto
    last_name: auto
    last_login: auto
    is_active: auto
    friends: List["UserType"] = strawberry.django.field(filters=UserFilter)


@strawberry.django.type(FriendRequest)
class FriendRequestType:
    id: strawberry.scalars.ID
    created_at: auto
    status: auto
    sender: UserType
