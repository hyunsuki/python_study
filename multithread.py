#!/usr/bin/python3
# -*- coding: utf-8 -*-

from multiprocessing import Process
from multiprocessing import Queue


class Bot(Process):

    def __init__(self, id_, start, end):
        self.total = 0
        self.id_ = id_
        self.start = start
        self.end = end
        self.result = Queue()
        super().__init__(target=self.work, args=(self.id_, self.start, self.end, self.result))

    def work(self):
        for i in range(self.start, self.end):
            self.total += i
        self.result.put(self.total)
        return

    def getResult(self):
        return self.result


def main():
    START = 0
    END = 1000000
    thread1 = Bot(1, START, END//2)
    thread2 = Bot(2, END//2, END)

    print(f"\nthread1 :: {thread1}")
    print(f"thread2 :: {thread2}\n")

    print(f"thread1's type :: {type(thread1)}")
    print(f"thread2's type :: {type(thread2)}\n")

    print(f"thread's dir :: {dir(thread1)}\n")

    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()

if __name__ == "__main__":
    main()
