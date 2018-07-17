# Example 2: asynchronous requests
import asyncio
import requests

async def main():
    loop = asyncio.get_event_loop()
    futures = [
        loop.run_in_executor(
            None,
            requests.get,
            'http://example.org/'
        )
        for i in range(10)
    ]
    for response in await asyncio.gather(*futures):
        print(response)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
