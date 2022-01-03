import asyncio

from hypercorn.asyncio import serve
from hypercorn.config import Config
from watchgod import awatch, DefaultWatcher

from social_media_backend.asgi import application as app


# Custom Watcher is needed to avoid files on venv
# Files on venv are avoided because they take too long to load
class CustomWatcher(DefaultWatcher):

    def __init__(self, root_path: str):
        self.ignored_dirs.add("venv")
        super().__init__(root_path)


# This function will be awaited and when resolved it will shut down the app
async def watch_changes():
    # If any source changes happen: breaking loop and returning
    async for changes in awatch('.', watcher_cls=CustomWatcher):
        break
    return True


# These are the configuration of the app
config = Config()
config.worker_class = "uvloop"

while True:
    loop = asyncio.get_event_loop()
    loop.set_debug(True)
    loop.run_until_complete(
        serve(app, config, shutdown_trigger=watch_changes)
    )