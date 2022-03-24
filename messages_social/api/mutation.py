from asgiref.sync import sync_to_async
from strawberry.types import Info
from strawberry_django_plus import gql

from messages_social.api.input import CreateMessageInput
from messages_social.api.types import MessagesType
from messages_social.models import Messages
from social_media_backend.api.utils import get_lazy_query_set_as_list
from user.api.utils import login_required_decorator


@gql.type
class Mutation:

    @gql.django.field
    @login_required_decorator
    async def create_message(self, info: Info, data: CreateMessageInput) -> MessagesType:
        user = info.variable_values.get("user")
        is_friend = await get_lazy_query_set_as_list(user.friends.filter(pk=data.receiver))
        if not is_friend:
            raise Exception("Receiver is not your friend")

        messages = await sync_to_async(Messages.objects.create)(receiver_id=data.receiver, sender=user,
                                                                content=data.content)
        return messages
