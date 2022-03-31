from dataclasses import dataclass
from typing import Union

from broadcaster import Broadcast
from django.http import HttpRequest, HttpResponse
from starlette.requests import Request
from starlette.responses import Response

broadcast = None


async def get_broadcast():
    global broadcast

    if not broadcast:
        broadcast = Broadcast("memory://")

        await broadcast.connect()

    return broadcast


@dataclass
class BroadcastContext:
    broadcast: Broadcast
    request: Union[Request, HttpRequest]
    response: Union[Response, HttpResponse]
