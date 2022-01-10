import strawberry.django
from strawberry.django import auto

from post.models import Post


@strawberry.django.type(Post)
class PostType:
    id: strawberry.scalars.ID
    description: auto
    publication_date: auto
    creation_date: auto
