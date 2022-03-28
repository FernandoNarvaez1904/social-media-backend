import strawberry
from strawberry_django_plus.optimizer import DjangoOptimizerExtension

from social_media_backend.api.mutation import Mutation
from social_media_backend.api.query import Query
from social_media_backend.api.subscription import Subscription

schema = strawberry.Schema(query=Query, mutation=Mutation, subscription=Subscription,
                           extensions=[DjangoOptimizerExtension])
