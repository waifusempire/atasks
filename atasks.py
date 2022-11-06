import asyncio
from typing import Coroutine, Optional


class Tasks:
    def __init__(self, catch_exceptions: bool = False) -> None:
        self._catch_exceptions = catch_exceptions
        self.__tasks: list[asyncio.Task] = []
        self.__results: list = []

    async def __aenter__(self):
        return self

    def create_task(self, coro: Coroutine, name: Optional[str] = None) -> None:
        if asyncio.iscoroutine(coro):
            self.__tasks.append(asyncio.create_task(coro, name=name))
        else:
            self.__results.append(coro)

    def sleep(self, delay: float):
        """The same as `~Tasks~.create_task(asyncio.sleep(delay))`"""
        self.create_task(asyncio.sleep(delay))

    async def __aexit__(self, *err):
        await self.resolve()

    async def resolve(self):
        self.__results.extend(
            await asyncio.gather(
                *self.__tasks, return_exceptions=self._catch_exceptions
            )
        )

    @property
    def results(self):
        return self.__results
