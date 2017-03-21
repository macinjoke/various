
def main():
    pass


class Human:

    def __init__(self, name, age):
        self.name = name
        self.age = age


class Alice(Human):

    def __init__(self, age):
        super(Alice, self).__init__(name='Alice', age=age)

    def execute(self):
        print("[EXECUTE] Alice")
        print("アリスは{}歳だぞ".format(self.age))


if __name__ == '__main__':
    main()
