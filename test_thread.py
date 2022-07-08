#!/usr/bin/python3
# -*- coding: utf-8 -*-


from threading import Thread


class Shared:
    resource = 0

    def __init__(self): pass


class MyThread(Thread):
    def __init__(self, threadID):
        Thread.__init__(self)
        self.threadID = threadID

    def run(self):
        print("Starting" + str(self.threadID))

        for i in range(1, 11):
            print(f"{self.threadID} {i}")
            Shared.resource += i*123456789
        print("Exiting" + str(self.threadID))
        print(f"Number :: {Shared.resource}")


def main():
    for i in range(1,1000001):
        thread = MyThread(i)
        thread.start()
#    thread1 = MyThread(1)
#    thread2 = MyThread(2)
#
#    thread1.start()
#    thread2.start()

if __name__ == '__main__':
    main()
