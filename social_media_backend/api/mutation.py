import strawberry

from post.api.mutations import Mutation as PostMutation
from user.api.mutation import Mutation as UserMutation


@strawberry.type
class Mutation(UserMutation, PostMutation):
    pass
