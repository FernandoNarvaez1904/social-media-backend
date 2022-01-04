import strawberry
import strawberry_django
from asgiref.sync import sync_to_async

from .types import User, CreateUserInput
from .utils import get_current_user_from_info
from ..models import User as UserModel


@strawberry.type
class Mutation:
    login: User = strawberry_django.auth.login()
    logout = strawberry_django.auth.logout()

    @strawberry_django.field
    async def create_user(self, data: CreateUserInput) -> User:
        user = await sync_to_async(UserModel.objects.create_user)(**data.__dict__)
        return user

    @strawberry_django.field
    async def delete_my_user(self, info, password: str) -> bool:
        user: UserModel = await get_current_user_from_info(info)
        if user.check_password(password):
            await sync_to_async(user.delete)()
            return True
        return False
