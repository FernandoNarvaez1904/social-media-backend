import strawberry
from strawberry.extensions import ParserCache, ValidationCache
from strawberry_django_plus.optimizer import DjangoOptimizerExtension

from social_media_backend.api.mutation import Mutation
from social_media_backend.api.query import Query

schema = strawberry.Schema(Query, Mutation, extensions=[ParserCache(), ValidationCache(), DjangoOptimizerExtension])
