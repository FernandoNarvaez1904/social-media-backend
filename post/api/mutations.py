import strawberry
import strawberry_django
from asgiref.sync import sync_to_async
from strawberry.types import Info

from post.api.input import CreatePostInput, DeletePostInput
from post.api.types import PostType
from post.models import Post
from social_media_backend.api.utils import clean_input_decorator, get_lazy_query_set_as_list
from user.api.utils import login_required_decorator


@strawberry.type
class Mutation:

    @strawberry_django.field
    @login_required_decorator
    @clean_input_decorator
    async def create_post(self, info, data: CreatePostInput) -> PostType:
        post = await sync_to_async(Post.objects.create)(**data.__dict__)
        return post

    @strawberry_django.field
    @login_required_decorator
    async def delete_post(self, info: Info, data: DeletePostInput) -> bool:
        user = info.variable_values.get("user")
        post = await get_lazy_query_set_as_list(user.my_posts.filter(pk=data.id))
        if not post:
            raise Exception(f"Post {data.id} does not exist")
        await sync_to_async(post[0].delete)()
        return True
