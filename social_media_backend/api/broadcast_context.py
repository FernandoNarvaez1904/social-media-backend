from dataclasses import dataclass
from typing import Union

from broadcaster import Broadcast
from strawberry.django.context import StrawberryDjangoContext

from user.models import User

broadcast = None


async def get_broadcast():
    global broadcast

    if not broadcast:
        broadcast = Broadcast("memory://")

        await broadcast.connect()

    return broadcast


@dataclass
class BroadcastContext(StrawberryDjangoContext):
    broadcast: Broadcast


@dataclass
class BroadcastContextWebsocket(StrawberryDjangoContext):
    broadcast: Broadcast
    user: Union[User, None]
