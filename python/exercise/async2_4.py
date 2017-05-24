
import asyncio
import requests

async def queue_execution(arg_urls, callback, parallel=2):
    loop = asyncio.get_event_loop()
    queue = asyncio.Queue()

    for url in arg_urls:
        queue.put_nowait(url)

    async def fetch(q):
        while not q.empty():
            url = await q.get()
            print(url)
            future = loop.run_in_executor(None, requests.get, url)
            future.add_done_callback(callback)
            await future

    tasks = [fetch(queue) for i in range(parallel)]
    return await asyncio.wait(tasks)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()

    results = []

    def store_result(f):
        results.append(f.result())
        print('Done', f)
    loop.run_until_complete(queue_execution([
        "http://www.google.com",
        "https://github.com/",
        "http://qiita.com/"
    ], store_result, 2))

    for r in results:
        print('queue execution: {}'.format(r.url))

