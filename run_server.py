import hypercorn.run
from hypercorn.config import Config
from social_media_backend.asgi import application as app
import asyncio
from hypercorn.asyncio import serve
from watchgod import awatch, DefaultWatcher

config = Config()
config.worker_class = "uvloop"

class CustomWatcher(DefaultWatcher):

    def __init__(self, root_path: str):
        self.ignored_dirs.add("venv")
        super().__init__(root_path)

async def start_new_loop(prev_loop = None, restart=False):
    if restart:
        prev_loop.close()

    new_loop = loop = asyncio.get_event_loop()
    new_loop.set_debug(True)
    return new_loop


async def main(loop):
    async for changes in awatch('.', watcher_cls=CustomWatcher):
        loop.run_until_complete(start_new_loop(loop, True))

loop = start_new_loop()
asyncio.run(main(loop))


