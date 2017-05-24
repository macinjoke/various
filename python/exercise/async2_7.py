
import asyncio
import requests


def get_async_iterator(arg_urls):

    class AsyncIterator:

        def __init__(self, urls):
            self.urls = iter(urls)
            self.__loop = None

        async def __aiter__(self):
            self.__loop = asyncio.get_event_loop()
            return self

        async def __anext__(self):
            try:
                u = next(self.urls)
                future = self.__loop.run_in_executor(None, requests.get, u)
                resp = await future
            except StopIteration:
                raise StopAsyncIteration
            return resp

    return AsyncIterator(arg_urls)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()

    async def async_fetch(urls):
        ai = get_async_iterator(urls)
        async for resp in ai:
            print(resp.url)

    loop.run_until_complete(async_fetch([
        "https://github.com/",
        "http://www.google.com",
        "http://qiita.com/"
    ]))






