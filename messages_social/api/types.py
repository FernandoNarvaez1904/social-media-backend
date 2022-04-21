from typing import List

from strawberry import ID
from strawberry_django_plus import gql

from messages_social.models import Messages, Conversation
from user.api.types import UserType


@gql.django.type(Conversation)
class ConversationType:
    id: gql.auto
    participants: List[UserType]
    messages: List["MessagesType"]


@gql.django.type(Messages)
class MessagesType:
    id: ID
    creation_date: gql.auto
    content: gql.auto
    received: gql.auto
    seen: gql.auto
    sender: UserType

    @gql.field
    async def conversation_id(self) -> str:
        return self.conversation_id
