import logging
logging.basicConfig(level=logging.DEBUG)


def main():
    logging.debug("main start")


class Human:

    def __init__(self, name, age):
        self.name = name
        self.age = age


class Alice(Human):

    def __init__(self, age):
        super(Alice, self).__init__(name='Alice', age=age)

    def execute(self):
        logging.debug("[EXECUTE] Alice")
        print("アリスは{}歳だぞ".format(self.age))


if __name__ == '__main__':
    main()
