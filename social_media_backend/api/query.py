from strawberry_django_plus import gql

from messages_social.api.query import Query as MessagesQuery
from user.api.query import Query as UserQuery


@gql.type
class Query(UserQuery, MessagesQuery):
    pass
