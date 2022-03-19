from strawberry_django_plus import gql

from user.api.query import Query as UserQuery


@gql.type
class Query(UserQuery):
    pass
