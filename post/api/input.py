from typing import Optional

import strawberry_django
from strawberry.django import auto
from strawberry.schema.types.base_scalars import DateTime

from post.models import Post


@strawberry_django.input(Post)
class CreatePostInput:
    description: auto
    publication_date: Optional[DateTime]


@strawberry_django.input(Post)
class DeletePostInput:
    id: auto
