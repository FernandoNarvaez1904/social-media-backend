import cProfile
import functools


def profile_on_terminal_decorator(func):
    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        with cProfile.Profile() as pr:
            f = await func(*args, **kwargs)
        pr.print_stats()
        return f

    return wrapper
