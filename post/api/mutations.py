from asgiref.sync import sync_to_async
from strawberry.types import Info
from strawberry_django_plus import gql

from post.api.input import CreatePostInput, DeletePostInput, CreateCommentInput, DeleteCommentInput
from post.api.types import PostType, CommentType
from social_media_backend.api.utils import clean_input_decorator, get_lazy_query_set_as_list
from user.api.utils import login_required_decorator
from user.models import User


@gql.type
class Mutation:

    @gql.django.field
    @login_required_decorator
    @clean_input_decorator
    async def create_post(self, info: Info, data: CreatePostInput) -> PostType:
        user: User = info.variable_values.get("user")
        post = await sync_to_async(user.my_posts.create)(**data.__dict__)
        return post

    @gql.django.field
    @login_required_decorator
    async def delete_post(self, info: Info, data: DeletePostInput) -> bool:
        user = info.variable_values.get("user")
        post = await get_lazy_query_set_as_list(user.my_posts.filter(pk=data.id))
        if not post:
            raise Exception(f"Post {data.id} does not exist")
        await sync_to_async(post[0].delete)()
        return True

    @gql.django.field
    @login_required_decorator
    async def create_comment(self, info: Info, data: CreateCommentInput) -> CommentType:
        user: User = info.variable_values.get("user")
        post = await sync_to_async(user.comments.create)(**data.__dict__)
        return post

    @gql.django.field
    @login_required_decorator
    async def delete_comment(self, info: Info, data: DeleteCommentInput) -> bool:
        my_user = info.variable_values.get("user")
        comment = await get_lazy_query_set_as_list(my_user.comments.filter(pk=data.id))
        if not comment:
            raise Exception(f"Post {data.id} does not exist")
        await sync_to_async(comment[0].delete)()
        return True
