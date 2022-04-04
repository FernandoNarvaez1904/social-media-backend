from asgiref.sync import sync_to_async

from ..models import User as UserModel


@sync_to_async
def get_current_user_from_info(info) -> UserModel:
    user = info.context.request.user
    # It forces the evaluation of the lazy model object
    if isinstance(user, UserModel):
        pass
    return user
