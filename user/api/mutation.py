import strawberry
from asgiref.sync import sync_to_async
from strawberry.django import auth
from strawberry_django import field

from .types import User, UserInput
from .utils import get_current_user_from_info
from ..models import User as UserModel


@strawberry.type
class Mutation:
    login: User = auth.login()
    logout = auth.logout()

    # TODO figure out why it drops server on debug
    @field
    async def create_user(self, data: UserInput) -> User:
        user = await sync_to_async(UserModel.objects.create_user)(**data.__dict__)
        return user

    @field
    async def delete_my_user(self, info, password: str) -> bool:
        user: UserModel = await get_current_user_from_info(info)
        if user.check_password(password):
            await sync_to_async(user.delete)()
            return True
        return False
