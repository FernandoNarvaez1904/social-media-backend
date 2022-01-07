from typing import List

import strawberry
import strawberry_django
from strawberry.types import Info

from .types import FriendRequestType, UserType
from .utils import login_required_decorator, get_lazy_query_set_as_list
from ..models import FriendRequest


@strawberry.type
class Query:

    @strawberry_django.field
    @login_required_decorator
    async def me(self, info: Info) -> UserType:
        user = info.variable_values.get("user")
        return user

    @strawberry_django.field
    @login_required_decorator
    async def pending_friend_request(self, info: Info) -> List[FriendRequestType]:
        user = info.variable_values.get("user")
        request_list = await get_lazy_query_set_as_list(
            user.receiver_friend_requests.filter(status=FriendRequest.RequestStatus.PENDING))
        return request_list
