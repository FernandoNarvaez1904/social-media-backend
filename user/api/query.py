import strawberry
import strawberry_django

from .types import User
from .utils import get_current_user_from_info


@strawberry.type
class Query:

    @strawberry_django.field
    async def me(self, info) -> User:
        user = await get_current_user_from_info(info)
        if not user.is_authenticated:
            raise Exception("User is not logged in")
        return user
