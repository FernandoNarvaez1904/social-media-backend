from typing import Optional

from strawberry.scalars import ID
from strawberry.schema.types.base_scalars import DateTime
from strawberry_django_plus import gql

from post.models import Post, Comment


@gql.django.input(Post)
class CreatePostInput:
    description: gql.auto
    publication_date: Optional[DateTime]


@gql.django.input(Post)
class DeletePostInput:
    id: gql.auto


@gql.django.input(Comment)
class CreateCommentInput:
    description: gql.auto
    post_id: ID


@gql.django.input(Comment)
class DeleteCommentInput:
    id: gql.auto
