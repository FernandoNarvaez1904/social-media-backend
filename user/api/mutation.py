import strawberry
import strawberry_django
from asgiref.sync import sync_to_async
from strawberry.types import Info

from .input import CreateUserInput, DeleteUserInput, SendFriendRequestInput, AcceptFriendRequestInput, \
    RejectFriendRequestInput
from .types import UserType
from .utils import login_required_decorator, get_lazy_query_set_as_list
from ..models import User


@strawberry.type
class Mutation:
    login: UserType = strawberry_django.auth.login()
    logout = strawberry_django.auth.logout()

    @strawberry_django.field
    async def create_user(self, info: Info, data: CreateUserInput) -> UserType:
        user = await sync_to_async(User.objects.create_user)(**data.__dict__)
        return user

    @strawberry_django.field
    @login_required_decorator
    async def delete_my_user(self, info: Info, data: DeleteUserInput) -> bool:
        user: User = info.variable_values.get("user")
        if user.check_password(data.password):
            await sync_to_async(user.delete)()
            return True
        return False

    @strawberry_django.field
    @login_required_decorator
    async def send_friend_request(self, info: Info, data: SendFriendRequestInput) -> bool:
        user: User = info.variable_values.get("user")
        receiver_user = await get_lazy_query_set_as_list(User.objects.filter(pk=data.userId))
        if not receiver_user:
            raise Exception(f"User with id {data.userId} does not exist")
        await sync_to_async(user.send_friend_request)(data.userId)
        return True

    @strawberry_django.field
    @login_required_decorator
    async def accept_friend_request(self, info: Info, data: AcceptFriendRequestInput) -> bool:
        user: User = info.variable_values.get("user")
        await sync_to_async(user.accept_friend_request)(data.requestId)
        return True

    @strawberry_django.field
    @login_required_decorator
    async def reject_friend_request(self, info: Info, data: RejectFriendRequestInput) -> bool:
        user: User = info.variable_values.get("user")
        await sync_to_async(user.reject_friend_request)(data.requestId)
        return True
