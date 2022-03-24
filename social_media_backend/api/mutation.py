from strawberry_django_plus import gql

from messages_social.api.mutation import Mutation as MessagesMutation
from user.api.mutation import Mutation as UserMutation


@gql.type
class Mutation(UserMutation, MessagesMutation):
    pass
