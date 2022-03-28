from strawberry_django_plus import gql

from messages_social.api.subscription import Subscription as MessagesSubscription


@gql.type
class Subscription(MessagesSubscription):
    pass
