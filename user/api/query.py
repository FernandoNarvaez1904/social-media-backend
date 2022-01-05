import strawberry
import strawberry_django

from .types import User
from .utils import get_current_user_from_info, login_required_decorator


@strawberry.type
class Query:

    @strawberry_django.field
    @login_required_decorator
    async def me(self, info) -> User:
        user = await get_current_user_from_info(info)
        return user

