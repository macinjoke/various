import time
from threading import Thread, Semaphore


class Task:
    def __init__(self, name, sleeptime):
        self.name = name
        self.sleeptime = sleeptime

    def run(self, semaphore):
        print(f'Start[{self.name}]: {self.sleeptime}')
        time.sleep(self.sleeptime)
        print(f'End[{self.name}]: {self.sleeptime}')
        semaphore.release()


if __name__ == '__main__':
    semaphore = Semaphore(2)
    task_list = [Task('a', 2), Task('b', 4), Task('c', 5), Task('d', 2)]
    for task in task_list:
        semaphore.acquire()
        Thread(target=task.run, args=(semaphore, )).start()
