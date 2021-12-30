import strawberry
import strawberry_django
from asgiref.sync import sync_to_async

from .types import User


@strawberry.type
class Query:

    @strawberry_django.field
    async def me(self, info) -> User:
        @sync_to_async()
        def get_user_in_request() -> User:
            return info.context.request.user
        print("got here")
        user = await get_user_in_request()
        if not user.is_authenticated:
            raise Exception("User is not logged in")
        return user
