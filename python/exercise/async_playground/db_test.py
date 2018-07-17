from sqlalchemy import create_engine

if __name__ == '__main__':
    engine = create_engine('mysql+pymysql://root:root@localhost/mydb?charset=utf8')

    result = engine.execute(f"select name, (x - 100) * (x - 100) + (y - 30) * (y - 30) as distance from toilets order by distance;")
    result_str = ""
    for row in result:
        print(row)
        result_str += str(row)

    print(result_str)
