from typing import List

from strawberry.types import Info
from strawberry_django_plus import gql

from social_media_backend.api.utils import get_lazy_query_set_as_list
from .filter import UserFilter
from .types import FriendRequestType, UserType
from .utils import login_required_decorator, get_current_user_from_info
from ..models import FriendRequest


@gql.type
class Query:
    users: List[UserType] = gql.django.field(filters=UserFilter)

    @gql.django.field
    async def is_logged_in(self, info: Info) -> bool:
        user = await get_current_user_from_info(info)
        return user.is_authenticated

    @gql.django.field
    @login_required_decorator
    async def me(self, info: Info) -> UserType:
        user = info.variable_values.get("user")
        return user

    @gql.django.field
    @login_required_decorator
    async def pending_friend_request(self, info: Info) -> List[FriendRequestType]:
        user = info.variable_values.get("user")
        request_list = await get_lazy_query_set_as_list(
            user.receiver_friend_requests.filter(status=FriendRequest.RequestStatus.PENDING))
        return request_list
