#!/usr/bin/python3
# -*- coding: utf-8 -*-


class Test:
    def __init__(self):
        self.a = None
        self.b = None
        self.c = ''
        self.__setting()

    def setValue(self, argu, default):
        print(f"{argu} is None :: {argu is None}")
        return default if argu is None or argu == "" else argu

    def __setting(self):
        self.setValue(self.a, 'test')
        self.setValue(self.b, 'test')
        self.setValue(self.c, 'test')

    def getList(self):
        return list(self.__dict__.values())


def main():
    t = Test()
    print(f"t.getList() :: {t.getList()}")


if __name__ == "__main__":
    main()
