from dataclasses import dataclass

from broadcaster import Broadcast
from strawberry.django.context import StrawberryDjangoContext

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
