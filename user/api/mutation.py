import strawberry
import strawberry_django
from asgiref.sync import sync_to_async

from .input import CreateUserInput, DeleteUserInput, SendFriendRequestInput
from .types import UserType
from .utils import get_current_user_from_info, login_required_decorator, get_lazy_query_set_as_list
from ..models import User


@strawberry.type
class Mutation:
    login: UserType = strawberry_django.auth.login()
    logout = strawberry_django.auth.logout()

    @strawberry_django.field
    async def create_user(self, data: CreateUserInput) -> UserType:
        user = await sync_to_async(User.objects.create_user)(**data.__dict__)
        return user

    @strawberry_django.field
    @login_required_decorator
    async def delete_my_user(self, info, data: DeleteUserInput) -> bool:
        user: User = await get_current_user_from_info(info)
        if user.check_password(data.password):
            await sync_to_async(user.delete)()
            return True
        return False

    @strawberry_django.field
    @login_required_decorator
    async def send_friend_request(self, info, data: SendFriendRequestInput) -> bool:
        user: User = await get_current_user_from_info(info)
        receiver_user = await get_lazy_query_set_as_list(User.objects.filter(pk=data.user_id))
        if not receiver_user:
            raise Exception(f"User with id {data.user_id} does not exist")
        await sync_to_async(user.send_friend_request)(data.user_id)
        return True
