#!/usr/bin/python3
# -*- coding: utf-8 -*-

import time
import queue
import threading


class Bot(threading.Thread):
    START_NUM = 0

    def __new__(cls):
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        cls = type(self)
        if not hasattr(cls, "_init"):
            cls._init = True

            threading.Thread.__init__(self, daemon=True)
            self.queue = queue.Queue()
            self.is_shutdown = False

    # Thread's job
    def run(self):
        while not self.is_shutdown:
            # must add do something
            Bot.START_NUM += 1
            print(f"Bot.START_NUM :: {Bot.START_NUM}")
            time.sleep(0.01)

    def setShutdown(self):
        self.is_shutdown = True


def main():
    # create two bots
    bot1 = Bot()
    bot2 = Bot()

    # singleton check
    print(f"id(bot1)==id(bot2) :: {id(bot1)==id(bot2)}")

    # bot1 thread run
    bot1.start()
    time.sleep(0.1)
    bot1.setShutdown()
    bot1.join()

    # bot2 thread run
    bot2.start()
    time.sleep(0.1)
    bot2.setShutdown()
    bot2.join()


if __name__ == "__main__":
    main()
