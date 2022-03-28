import typing

from starlette.requests import Request
from starlette.responses import Response
from starlette.websockets import WebSocket
from strawberry.asgi import GraphQL

from .broadcast_context import BroadcastContext, get_broadcast


class MyGraphQL(GraphQL):
    async def get_context(self, request: typing.Union[Request, WebSocket],
                          response: typing.Optional[Response] = None, ) -> typing.Optional[typing.Any]:
        broadcast = await get_broadcast()

        return BroadcastContext(broadcast=broadcast, request=request, response=response)
