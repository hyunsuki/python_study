#!/usr/bin/python3
# -*- coding: utf-8 -*-

import multiprocessing


class Bot(multiprocessing.Process):

    def __init__(self, word):
        multiprocessing.Process.__init__(self, target=self.worker, args=(word,))

    def worker(self, word):
        print(f"word :: {word}")


def main():
    bot = Bot('hyunsuki')
    print(f"bot :: {type(bot)}")
    print("Test code :: bot.start()")
    bot.start()
    bot.join()


if __name__ == "__main__":
    main()
