from typing import Optional, List

from django.contrib.auth import get_user_model
from strawberry.scalars import ID
from strawberry_django_plus import gql


@gql.django.input(get_user_model())
class CreateUserInput:
    username: gql.auto
    password: gql.auto
    email: gql.auto
    first_name: gql.auto
    last_name: gql.auto


@gql.django.input(get_user_model())
class UpdateUserInput:
    first_name: Optional[str]
    last_name: Optional[str]
    last_name: Optional[str]


@gql.django.input(get_user_model())
class DeleteUserInput:
    password: gql.auto


@gql.input
class SendFriendRequestInput:
    userId: ID


@gql.input
class AcceptFriendRequestInput:
    requestId: ID


@gql.input
class RejectFriendRequestInput:
    requestId: ID


@gql.input
class RemoveFriendsInput:
    friends_id: List[ID]
