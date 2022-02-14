from typing import List

from django.contrib.auth import get_user_model
from strawberry import ID
from strawberry_django_plus import gql

from .filter import UserFilter
from ..models import FriendRequest


@gql.django.type(get_user_model())
class UserType:
    id: ID
    username: gql.auto
    email: gql.auto
    first_name: gql.auto
    last_name: gql.auto
    last_login: gql.auto
    is_active: gql.auto
    friends: List["UserType"] = gql.django.field(filters=UserFilter)


@gql.django.type(FriendRequest)
class FriendRequestType:
    id: ID
    created_at: gql.auto
    status: gql.auto
    sender: UserType
