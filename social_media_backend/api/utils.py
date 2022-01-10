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


# Deletes all unset values in an input type
def clean_input_decorator(func):
    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        for val in kwargs.values():
            if hasattr(val, "_django_type") and val._django_type.is_input:
                for key, field in val.__dict__.copy().items():
                    if not field:
                        delattr(val, key)
        r = await func(*args, **kwargs)
        return r

    return wrapper


async def get_lazy_query_set_as_list(query_set: QuerySet) -> List:
    list_coroutine = sync_to_async(list)
    return await list_coroutine(query_set)
