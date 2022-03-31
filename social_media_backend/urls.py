from django.urls import path

from social_media_backend.api.custom_graphql_config import AsyncGraphQLViewWithBroadcast
from social_media_backend.api.schema import schema

urlpatterns = [
    path("graphql/", AsyncGraphQLViewWithBroadcast.as_view(schema=schema)),
]
