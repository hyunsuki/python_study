#!/usr/bin/python3
# -*- coding: utf-8 -*-


class Test:

    def __new__(cls):
        if not hasattr(cls, "_instance"):
            print("__new__ is called\n")
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        cls = type(self)
        if not hasattr(cls, "_init"):
            print("__init__ is called\n")
            cls._init = True

    def initTest(self, only_init=True):
        cls = type(self)
        if only_init == False:
            if hasattr(cls, "_instance"): del cls._instance
        if hasattr(cls, "_init"): del cls._init


def main():
    singleton1 = Test()
    singleton2 = Test()
    print(f"sigleton1's id :: {id(singleton1)}")
    print(f"sigleton2's id :: {id(singleton2)}")
    Test().initTest()
    singleton3 = Test()
    print(f"sigleton2's id :: {id(singleton2)}")


if __name__ == '__main__':
    main()
