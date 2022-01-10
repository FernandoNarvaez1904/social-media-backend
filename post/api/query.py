from typing import List

import strawberry
from strawberry.types import Info

from post.api.types import PostType
from social_media_backend.api.utils import get_lazy_query_set_as_list
from user.api.utils import login_required_decorator


@strawberry.type
class Query:

    @strawberry.field
    @login_required_decorator
    async def my_posts(self, info: Info) -> List[PostType]:
        user = info.variable_values.get("user")
        post = await get_lazy_query_set_as_list(user.my_posts.all())
        return post
