import attr


def auto_validate(cls):
    class Decorated(cls):
        def __setattr__(self, name, value):
            super().__setattr__(name, value)
            attr.validate(self)
    return Decorated


@auto_validate
# @attr.s(frozen=True)
@attr.s
class Hoge:
    a = attr.ib(validator=attr.validators.instance_of(int))



hoge1 = Hoge(1)
print(hoge1)
# hoge2 = Hoge("1")
# print(hoge2)
hoge1.a = "1"













