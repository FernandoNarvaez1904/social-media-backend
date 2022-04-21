from typing import List, Optional

from asgiref.sync import sync_to_async
from strawberry.types import Info
from strawberry_django_jwt.decorators import login_required
from strawberry_django_plus import gql

from messages_social.api.types import ConversationType
from messages_social.models import Conversation
from social_media_backend.api.utils import get_lazy_query_set_as_list
from user.api.utils import get_current_user_from_info
from user.models import User


@gql.type
class Query:

    @gql.django.field
    @login_required
    async def my_conversations(self, info: Info, other_id: Optional[str]) -> List[ConversationType]:
        user = await get_current_user_from_info(info)

        if not other_id:
            return await get_lazy_query_set_as_list(Conversation.objects.filter(participants__in=[user]))

        other = await sync_to_async(User.objects.get)(id=other_id)
        return await get_lazy_query_set_as_list(Conversation.objects.filter(participants__in=[user, other]))
