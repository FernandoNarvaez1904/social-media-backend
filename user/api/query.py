from typing import List

import strawberry
import strawberry_django

from .utils import get_current_user_from_info, login_required_decorator


@strawberry.type
class Query:

    @strawberry_django.field
    @login_required_decorator
    async def me(self, info) -> UserType:
        user = await get_current_user_from_info(info)
        return user

    @strawberry_django.field
    @login_required_decorator
    async def pending_friend_request(self, info) -> List[FriendRequestType]:
        user = await get_current_user_from_info(info)
        request_list = await get_lazy_query_set_as_list(
            user.receiver_friend_requests.filter(status=FriendRequest.RequestStatus.PENDING))
        return request_list
