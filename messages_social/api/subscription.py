from typing import List

import strawberry
from asgiref.sync import sync_to_async
from strawberry.types import Info
from strawberry_django_plus import gql

from messages_social.api.types import MessagesType
from messages_social.models import Messages


@gql.type
class Subscription:

    @strawberry.subscription
    async def room_messages(self, info: Info, chatroom_id: str) -> List[MessagesType]:
        async with info.context.broadcast.subscribe(channel=f"chatroom-{chatroom_id}") as subscriber:
            async for event in subscriber:
                message: Messages = await sync_to_async(Messages.objects.get)(pk=event.message)
                yield [message]
