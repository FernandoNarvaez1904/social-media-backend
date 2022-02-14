from typing import List

from strawberry.scalars import ID
from strawberry_django_plus import gql

from post.models import Post, Comment
from user.api.types import UserType


@gql.django.type(Post)
class PostType:
    id: ID
    description: gql.auto
    publication_date: gql.auto
    creation_date: gql.auto
    comments: List["CommentType"]
    user: UserType


@gql.django.type(Comment)
class CommentType:
    id: ID
    description: gql.auto
    post: PostType
    user: UserType
