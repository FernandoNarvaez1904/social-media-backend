import cProfile
import functools
from typing import List

from asgiref.sync import sync_to_async
from django.db.models import QuerySet


def profile_on_terminal_decorator(func):
    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        with cProfile.Profile() as pr:
            f = await func(*args, **kwargs)
        pr.print_stats()
        return f

    return wrapper


async def get_lazy_query_set_as_list(query_set: QuerySet) -> List:
    list_coroutine = sync_to_async(list)
    return await list_coroutine(query_set)
