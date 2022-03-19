from strawberry_django_plus import gql

from user.api.mutation import Mutation as UserMutation


@gql.type
class Mutation(UserMutation):
    pass
