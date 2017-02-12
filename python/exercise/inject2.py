# reference
# http://injector.readthedocs.io/en/latest/testing.html

import unittest
from injector import Module, with_injector, inject


class UsernameModule(Module):
    def configure(self, binder):
        binder.bind(str, 'Maria')


class TestSomethingClass(unittest.TestCase):
    @with_injector(UsernameModule())
    def setUp(self):
        pass

    @inject(username=str)
    def test_username(self, username):
        self.assertEqual(username, 'Maria')


