MySQLにダミーデータをINSERTする
```shell
$ docker-compose exec mysql mysql -u root -D mydb --password=root -e"$(cat db/sql/insert_dummy.sql)"
```
