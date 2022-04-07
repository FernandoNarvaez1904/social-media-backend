from typing import List

import strawberry
from asgiref.sync import sync_to_async
from strawberry.types import Info
from strawberry_django_plus import gql

from messages_social.api.types import MessagesType
from messages_social.models import Messages
from user.models import User


@gql.type
class Subscription:

    @strawberry.subscription
    async def my_messages(self, info: Info) -> List[MessagesType]:
        user: User = info.context.get("user")
        async with info.context.broadcast.subscribe(channel=f"chatroom-{user.id}") as subscriber:
            async for event in subscriber:
                message: Messages = await sync_to_async(Messages.objects.get)(pk=event.message)
                message.received = True
                await sync_to_async(message.save)()
                yield [message]
