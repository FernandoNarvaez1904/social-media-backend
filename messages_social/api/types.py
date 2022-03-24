from strawberry import ID
from strawberry_django_plus import gql

from messages_social.models import Messages
from user.api.types import UserType


@gql.django.type(Messages)
class MessagesType:
    id: ID
    sender: UserType
    receiver: UserType
    creation_date: gql.auto
    content: gql.auto
    received: gql.auto
    seen: gql.auto
