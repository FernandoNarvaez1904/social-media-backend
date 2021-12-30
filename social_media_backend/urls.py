from django.urls import path

from strawberry.django.views import AsyncGraphQLView

from social_media_backend.api.schema import schema

urlpatterns = [
    path("graphql/", AsyncGraphQLView.as_view(schema=schema)),
    "he"
]
