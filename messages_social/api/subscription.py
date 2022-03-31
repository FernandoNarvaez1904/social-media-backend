import strawberry
from asgiref.sync import sync_to_async
from strawberry.types import Info
from strawberry_django_plus import gql

from messages_social.api.types import MessagesType
from messages_social.models import Messages
from user.api.utils import login_required_decorator
from user.models import User


@gql.type
class Subscription:

    @strawberry.subscription
    @login_required_decorator
    async def my_messages(self, info: Info) -> MessagesType:
        user: User = info.variable_values.get("user")
        async with info.context.broadcast.subscribe(channel=f"chatroom-{user.id}") as subscriber:
            async for event in subscriber:
                yield sync_to_async(Messages.objects.get)(pk=event.message)
