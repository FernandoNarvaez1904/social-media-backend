import strawberry

from post.api.query import Query as PostQuery
from user.api.query import Query as UserQuery


@strawberry.type
class Query(UserQuery, PostQuery):
    pass
