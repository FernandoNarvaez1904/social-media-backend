import strawberry.django
from strawberry.django import auto

from post.models import Post, Comment
from user.api.types import UserType


@strawberry.django.type(Post)
class PostType:
    id: strawberry.scalars.ID
    description: auto
    publication_date: auto
    creation_date: auto
