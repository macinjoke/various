from injector import Key, ClassAssistedBuilder, AssistedBuilder, Injector, inject


class Database: pass


class User:
    def __init__(self, name):
        self.name = name


class UserUpdater:
    def __init__(self, db: Database, user):
        pass


# class NeedsUserUpdater:
#     @inject
#     def __init__(self, builder: ClassAssistedBuilder[UserUpdater]):
#         self.updater_builder = builder
#
#     def method(self):
#         updater = self.updater_builder.build(user=None)


if __name__ == '__main__':
    injector = Injector()
    builder = injector.get(ClassAssistedBuilder[UserUpdater])
    user = User('John')
    user_updater = builder.build(user=user)