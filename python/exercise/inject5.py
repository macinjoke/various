from injector import Key, ClassAssistedBuilder, AssistedBuilder, Injector, inject

DB = Key('DB')


class DBImplementation:
    def __init__(self, uri):
        pass


def configure(binder):
    binder.bind(DB, to=DBImplementation)


if __name__ == '__main__':

    # injector = Injector()
    # builder = injector.get(ClassAssistedBuilder[UserUpdater])
    # user = User('John')
    # user_updater = builder.build(user=user)

    print("aaa")
    injector = Injector(configure)
    builder = injector.get(AssistedBuilder[DB])
    # print(isinstance(builder.build(uri='x'), DBImplementation))