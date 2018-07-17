import asyncio
import requests
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import datetime

engine = create_engine('mysql+pymysql://root:root@localhost/mydb?charset=utf8')
Session = sessionmaker(bind=engine)
session = Session()

# http request を実行する
def http_request(start_time, url):
    print("start http_request")
    result = requests.get(url)
    elapsed = datetime.datetime.now().timestamp() - start_time
    print("end http_request, 経過時間:", elapsed)
    return result

# database へSQLを発行する
def execute_sql(start_time, query, dictionary):
    print("start execute_sql")
    result = session.execute(query, dictionary)
    elapsed = datetime.datetime.now().timestamp() - start_time
    print("end execute_sql,  経過時間:", elapsed)
    return result

# 並列実行
async def execute_async(start_time):
    loop = asyncio.get_event_loop()
    import concurrent.futures
    import os
    print(os.cpu_count())
    executor = concurrent.futures.ThreadPoolExecutor()
    print(executor._max_workers)
    print()
    futures = [
        loop.run_in_executor(
            None,
            http_request,
            start_time,
            'http://example.org/'
        )
        for i in range(3)
    ]

    futures.extend([loop.run_in_executor(
        None,
        execute_sql,
        start_time,
        "select * from users where name like :string ;",
        {'string': "%ck"}
    ) for i in range(3)])

    await asyncio.gather(*futures)

# 逐次実行
def execute_sync(start_time):
    for i in range(3):
        http_request(start_time, 'http://example.org/')

    for i in range(3):
        execute_sql(
            start_time,
            "select * from users where name like :string ;",
            {'string': "%ck"}
        )

if __name__ == '__main__':
    # 並列に実行
    print("並列実行")
    loop = asyncio.get_event_loop()
    loop.run_until_complete(execute_async(datetime.datetime.now().timestamp()))
    loop.close()

    print()

    # 逐次実行
    print("逐次実行")
    execute_sync(datetime.datetime.now().timestamp())
