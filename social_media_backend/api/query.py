from strawberry_django_plus import gql

from post.api.query import Query as PostQuery
from user.api.query import Query as UserQuery


@gql.type
class Query(UserQuery, PostQuery):
    pass
