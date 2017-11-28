import attr


def main():
    sc1 = SomeClass(1, [1, 2, 3])
    print(sc1 == SomeClass(1, [1, 2, 3]))
    print(sc1)
    print(sc1.hard_math(2))

    # sc2 = SomeClass()
    # print(sc2)

    C1 = attr.make_class("C1", ["x", "y"])
    c1 = C1(1, 2)
    print(c1)

@attr.s
class SomeClass:
    a_number = attr.ib(default=42)
    list_of_numbers = attr.ib(default=attr.Factory(list))

    def hard_math(self, another_number):
        return self.a_number + sum(self.list_of_numbers) * another_number


# class SomeClass:
#
#     def __init__(self, a_number=42, list_of_numbers=[]):
#         self.a_number = a_number
#         self.list_of_numbers = list_of_numbers
#
#     def hard_math(self, another_number):
#         return self.a_number + sum(self.list_of_numbers) * another_number

if __name__ == '__main__':
    main()
