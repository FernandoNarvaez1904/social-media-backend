import functools
from typing import Callable

from asgiref.sync import sync_to_async

from ..models import User as UserModel


@sync_to_async
def get_current_user_from_info(info) -> UserModel:
    user = info.context.request.user
    # It forces the evaluation of the lazy model object
    if isinstance(user, UserModel):
        pass
    return user


def login_required_decorator(func):
    @functools.wraps(func)
    async def wrapper(*args, **kwargs) -> Callable:
        user = await get_current_user_from_info(kwargs.get("info"))
        if not user.is_authenticated:
            raise Exception("User is not logged in")
        kwargs["info"].variable_values["user"] = user
        return await func(*args, **kwargs)

    return wrapper
