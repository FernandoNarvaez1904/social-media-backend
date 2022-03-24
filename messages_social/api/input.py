from strawberry_django_plus import gql

from messages_social.models import Messages


@gql.django.input(Messages)
class CreateMessageInput:
    receiver: gql.ID
    content: gql.auto
