from typing import List

from strawberry.types import Info
from strawberry_django_jwt.decorators import login_required
from strawberry_django_plus import gql

from messages_social.api.types import ConversationType
from messages_social.models import Conversation
from social_media_backend.api.utils import get_lazy_query_set_as_list
from user.api.utils import get_current_user_from_info


@gql.type
class Query:

    @gql.django.field
    @login_required
    async def my_conversations(self, info: Info) -> List[ConversationType]:
        user = await get_current_user_from_info(info)
        return await get_lazy_query_set_as_list(Conversation.objects.filter(participants__in=[user]))
