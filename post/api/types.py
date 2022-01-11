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


@strawberry.django.type(Comment)
class CommentType:
    id: strawberry.scalars.ID
    description: auto
    post: PostType
    user: UserType
