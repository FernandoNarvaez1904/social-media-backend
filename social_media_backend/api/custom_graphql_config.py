import os
import typing

from asgiref.sync import sync_to_async

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "social_media_backend.settings")
import django

django.setup()
from django.http import HttpRequest, HttpResponse
from starlette.requests import Request
from starlette.responses import Response
from starlette.websockets import WebSocket
from strawberry.asgi import GraphQL
from strawberry.django.views import AsyncGraphQLView

from user.models import User
from .broadcast_context import BroadcastContext, get_broadcast, BroadcastContextWebsocket


class WebSocketGraphQL(GraphQL):
    async def get_context(self, request: typing.Union[Request, WebSocket, HttpRequest],
                          response: typing.Optional[Response] = None, ) -> typing.Optional[typing.Any]:
        broadcast = await get_broadcast()

        user_data = request.scope.get("params_dict")
        user_final = None
        if user := await sync_to_async(User.objects.get)(username=user_data.get("username")):
            if await sync_to_async(user.check_password)(user_data.get("password")):
                user_final = user

        return BroadcastContextWebsocket(broadcast=broadcast, request=request, response=response, user=user_final)


class AsyncGraphQLViewWithBroadcast(AsyncGraphQLView):
    async def get_context(self, request: HttpRequest, response: HttpResponse) -> typing.Any:
        broadcast = await get_broadcast()

        return BroadcastContext(broadcast=broadcast, request=request, response=response)
