# reference
# https://pythonhosted.org/injector/

from injector import Module, Key, provides, Injector, inject, singleton

import sqlite3


class RequestHandler:
    # @inject(db=sqlite3.Connection)
    # def __init__(self, db):
    @inject
    def __init__(self, db: sqlite3.Connection):
        self._db = db

    def get(self):
        cursor = self._db.cursor()
        cursor.execute('SELECT key, value FROM data ORDER by key')
        return cursor.fetchall()

Configuration = Key('configuration')


class ConfigurationForTestingModule(Module):
    def configure(self, binder):
        binder.bind(Configuration, to={'db_connection_string': ':memory:'}, scope=singleton)


class DatabaseModule(Module):
    @singleton
    @provides(sqlite3.Connection)
    # @inject(configuration=Configuration)
    # def provide_sqlite_connection(self, configuration):
    @inject
    def provide_sqlite_connection(self, configuration: Configuration):
        conn = sqlite3.connect(configuration['db_connection_string'])
        cursor = conn.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS data (key PRIMARY KEY, value)')
        cursor.execute('INSERT OR REPLACE INTO data VALUES ("A", "hoge")')
        cursor.execute('INSERT OR REPLACE INTO data VALUES ("B", "fuga")')
        return conn

injector = Injector([ConfigurationForTestingModule(), DatabaseModule()])


class Tekitou:
    # @inject(db=sqlite3.Connection)
    # def __init__(self, db):
    @inject
    def __init__(self, s: str):
        self._s = s

    def get(self):
        return "self._s: " + self._s


handler = injector.get(RequestHandler)
print(handler.get())

