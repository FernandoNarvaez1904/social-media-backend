import strawberry
import strawberry_django
from asgiref.sync import sync_to_async

from post.api.input import CreatePostInput
from post.api.types import PostType
from post.models import Post
from social_media_backend.api.utils import clean_input_decorator
from user.api.utils import login_required_decorator


@strawberry.type
class Mutation:

    @strawberry_django.field
    @login_required_decorator
    @clean_input_decorator
    async def create_post(self, info, data: CreatePostInput) -> PostType:
        post = await sync_to_async(Post.objects.create)(**data.__dict__)
        return post
