from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
import random
import string

engine = create_engine('mysql+pymysql://root:root@localhost/mydb?charset=utf8')
Session = sessionmaker(bind=engine)


random_strs = [
    ''.join([
        random.choice(string.ascii_lowercase) for i in range(20)
    ]) for i in range(10000)
]
insert_data = [{
    'name': random_strs[i],
    'gender': random.choice(['man', 'woman']),
    'age': random.randint(10, 90)
} for i in range(10000)]


session = Session()
for i in range(10000):
    print(i)
    session.execute(
        "insert into users (name, gender, age, with_children) values (:name, :gender, :age, false);",
        {
            'name': insert_data[i]['name'],
            'gender': insert_data[i]['gender'],
            'age': insert_data[i]['age']
        }
    )
