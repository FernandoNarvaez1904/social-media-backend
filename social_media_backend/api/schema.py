import strawberry
from strawberry.extensions import ParserCache, ValidationCache

from social_media_backend.api.mutation import Mutation
from social_media_backend.api.query import Query

schema = strawberry.Schema(Query, Mutation, extensions=[ParserCache(), ValidationCache()])
