import asyncio
from unittest import TestCase
from unittest.mock import Mock

class AioTestCase(TestCase):
    
    # noinspection PyPep8Naming
    def __init__(self, methodName='runTest', loop=None):
        self.loop = loop or asyncio.get_event_loop()
        self._function_cache = {}
        super(AioTestCase, self).__init__(methodName=methodName)

    def coroutine_function_decorator(self, func):
        def wrapper(*args, **kw):
            cor = func(*args, **kw)
            return self.loop.run_until_complete(cor)
        return wrapper

    def __getattribute__(self, item):
        attr = object.__getattribute__(self, item)
        if asyncio.iscoroutinefunction(attr):
            if item not in self._function_cache:
                self._function_cache[item] = self.coroutine_function_decorator(attr)
            return self._function_cache[item]
        # print(attr, type(attr))
        return attr

class AsyncMock(Mock):

    def __call__(self, *args, **kwargs):
        sup = super(AsyncMock, self)
        async def coro():
            return sup.__call__(*args, **kwargs)
        return coro()

    def __await__(self):
        return self().__await__()


class EmptyAsyncMock(Mock):

    def __call__(self, *args, **kwargs):
        sup = super(EmptyAsyncMock, self)
        async def coro():
            return None
        return coro()

    def __await__(self):
        return self().__await__()
