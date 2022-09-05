#!/usr/bin/python3

import sys


class Test:
    def __init__(self, argu):
        self.__argu = argu

    def getArgu(self):
        return self.__argu

    def setArgu(self, argu):
        self.__argu = argu


def main():
    t = Test()


if __name__ == "__main__":
    main()
