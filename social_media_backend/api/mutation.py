from strawberry_django_plus import gql

from post.api.mutations import Mutation as PostMutation
from user.api.mutation import Mutation as UserMutation


@gql.type
class Mutation(UserMutation, PostMutation):
    pass
