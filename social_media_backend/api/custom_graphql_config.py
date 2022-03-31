import typing

from django.http import HttpRequest, HttpResponse
from starlette.requests import Request
from starlette.responses import Response
from starlette.websockets import WebSocket
from strawberry.asgi import GraphQL
from strawberry.django.views import AsyncGraphQLView

from .broadcast_context import BroadcastContext, get_broadcast


class WebSocketGraphQL(GraphQL):
    async def get_context(self, request: typing.Union[Request, WebSocket],
                          response: typing.Optional[Response] = None, ) -> typing.Optional[typing.Any]:
        broadcast = await get_broadcast()

        return BroadcastContext(broadcast=broadcast, request=request, response=response)


class AsyncGraphQLViewWithBroadcast(AsyncGraphQLView):
    async def get_context(self, request: HttpRequest, response: HttpResponse) -> typing.Any:
        broadcast = await get_broadcast()

        return BroadcastContext(broadcast=broadcast, request=request, response=response)
