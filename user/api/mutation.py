import strawberry_django_jwt.mutations as jwt_mutations
from asgiref.sync import sync_to_async
from strawberry.types import Info
from strawberry_django_jwt.decorators import login_required
from strawberry_django_plus import gql

from social_media_backend.api.utils import get_lazy_query_set_as_list
from .input import CreateUserInput, DeleteUserInput, SendFriendRequestInput, AcceptFriendRequestInput, \
    RejectFriendRequestInput, UpdateUserInput, RemoveFriendsInput
from .types import UserType
from .utils import get_current_user_from_info
from ..models import User


@gql.type
class Mutation:
    token_auth = jwt_mutations.ObtainJSONWebToken.obtain
    verify_token = jwt_mutations.Verify.verify
    refresh_token = jwt_mutations.Refresh.refresh
    delete_token_cookie = jwt_mutations.DeleteJSONWebTokenCookie.delete_cookie

    @gql.django.field
    async def create_user(self, info: Info, data: CreateUserInput) -> UserType:
        user = await sync_to_async(User.objects.create_user)(**data.__dict__)
        return user

    @gql.django.field
    @login_required
    async def update_user(self, info: Info, data: UpdateUserInput) -> UserType:
        user = await get_current_user_from_info(info)
        [user.__setattr__(key, val) if val else "" for key, val in data.__dict__.items()]
        await sync_to_async(user.save)()
        return user

    @gql.django.field
    @login_required
    async def delete_my_user(self, info: Info, data: DeleteUserInput) -> bool:
        user: User = await get_current_user_from_info(info)
        if user.check_password(data.password):
            await sync_to_async(user.delete)()
            return True
        return False

    @gql.django.field
    @login_required
    async def send_friend_request(self, info: Info, data: SendFriendRequestInput) -> bool:
        user: User = await get_current_user_from_info(info)
        receiver_user = await get_lazy_query_set_as_list(User.objects.filter(pk=data.userId))
        if not receiver_user:
            raise Exception(f"User with id {data.userId} does not exist")
        await sync_to_async(user.send_friend_request)(data.userId)
        return True

    @gql.django.field
    @login_required
    async def accept_friend_request(self, info: Info, data: AcceptFriendRequestInput) -> bool:
        user: User = await get_current_user_from_info(info)
        await sync_to_async(user.accept_friend_request)(data.requestId)
        return True

    @gql.django.field
    @login_required
    async def remove_friends(self, info: Info, data: RemoveFriendsInput) -> bool:
        user: User = await get_current_user_from_info(info)
        friends = await get_lazy_query_set_as_list(user.friends.filter(pk__in=data.friends_id))
        if friends:
            [await sync_to_async(user.friends.remove)(f) for f in friends]
            return True
        return False

    @gql.django.field
    @login_required
    async def reject_friend_request(self, info: Info, data: RejectFriendRequestInput) -> bool:
        user: User = await get_current_user_from_info(info)
        await sync_to_async(user.reject_friend_request)(data.requestId)
        return True
