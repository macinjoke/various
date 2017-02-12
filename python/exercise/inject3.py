from injector import inject, Injector, Module, Key, provider #, InstanceProvider
import time

Name = Key('name')
Description = Key('description')

# bindings = {
#     (Name, None): InstanceProvider('Sherlock'),
#     (Description, None): InstanceProvider('A man of astounding insight'),
# }


# class MyModule(Module):
#     def configure(self, binder):
#         binder.bind(Name, to='Sherlock')
#         binder.bind(Description, to='A man of astounding insight')


# class MyModule(Module):
#     def configure(self, binder):
#         binder.bind(Name, to='Sherlock')
#
#     @provider
#     def describe(self) -> Description:
#         return 'A man of astounding insight (at %s)' % time.time()


class User(object):
    @inject
    def __init__(self, name: Name, description: Description):
        self.name = name
        self.description = description


class UserModule(Module):
    def configure(self, binder):
        binder.bind(User)




class UserAttributeModule(Module):
    def configure(self, binder):
        binder.bind(Name, to='Sherlock')

    @provider
    def describe(self, name: Name) -> Description:
        return '%s is a man of astounding insight' % name


if __name__ == '__main__':
    # injecter = Injector([MyModule])
    # injecter = Injector([UserModule(), UserAttributeModule()])
    injecter = Injector([UserModule, UserAttributeModule])
    u = injecter.get(User)
    n = injecter.get(Name)
    d = injecter.get(Description)
    print("user: " + str(u))
    print("name: " + u.name)
    print("description: " + u.description)
    
    print("name: " + n)
    print("description: " + d)
