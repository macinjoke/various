
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from threading import Thread, BoundedSemaphore, Semaphore, Lock
from multiprocessing import Process
from collections import OrderedDict


colors = {
    'RED': '\033[31m',
    'GREEN': '\033[32m',
    'YELLOW': '\033[33m',
    'BLUE': '\033[34m',
    'PURPLE': '\033[35m',
    'CYAN': '\033[36m',
}


def color_print(text, color):
    print(f'{color}{text}\033[0m')


class Task:
    def __init__(self, name, complexity):
        self.name = name
        self.complexity = complexity

    def __call__(self, semaphore):
        color_print(
            f'Start[{self.name}]: {self.complexity}',
            tuple(colors.values())[int(self.name) % len(colors)]
        )
        time.sleep(self.complexity)
        color_print(
            f'Done [{self.name}]: {self.complexity}',
            tuple(colors.values())[int(self.name) % len(colors)]
        )
        for _ in range(2):
            semaphore.release()


class Dispatcher:
    def __init__(self, semaphore):
        self.semaphore = semaphore

    def dispatch(self, task_list):
        for task in task_list:
            self.semaphore.acquire()
            Thread(target=task, args=(self.semaphore, )).start()
            # Process(target=task, args=(self.semaphore, )).start()


if __name__ == '__main__':
    semaphore = BoundedSemaphore(1)
    dispatcher = Dispatcher(semaphore)
    # task_list = [
    #     Task('1', 10),
    #     Task('2', 16),
    #     Task('3', 4),
    #     Task('4', 8),
    #     Task('5', 6),
    #     Task('6', 2)
    # ]
    task_list = [
        Task('1', 2),
        Task('2', 2),
        Task('3', 2),
        Task('4', 2),
        Task('5', 2),
        Task('6', 2),
        Task('7', 2),
        Task('8', 2),
        Task('9', 2),
        Task('10', 2),
        Task('11', 2),
        Task('12', 2)
    ]
    dispatcher.dispatch(task_list)
