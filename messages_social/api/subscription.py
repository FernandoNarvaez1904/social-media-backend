from typing import List

import strawberry
from asgiref.sync import sync_to_async
from strawberry.types import Info
from strawberry_django_plus import gql

from messages_social.api.types import MessagesType
from messages_social.models import Messages
from social_media_backend.api.utils import get_lazy_query_set_as_list
from user.models import User


@gql.type
class Subscription:

    @strawberry.subscription
    async def my_messages(self, info: Info) -> List[MessagesType]:

        user: User = info.context.get("user")

        not_received_messages = await get_lazy_query_set_as_list(
            Messages.objects.filter(received=False, receiver_id=user.id))
        if not_received_messages:
            for message in not_received_messages:
                message.received = True
                await sync_to_async(message.save)()
            yield not_received_messages

        async with info.context.broadcast.subscribe(channel=f"chatroom-{user.id}") as subscriber:
            async for event in subscriber:
                message: Messages = await sync_to_async(Messages.objects.get)(pk=event.message)
                message.received = True
                await sync_to_async(message.save)()
                yield [message]
