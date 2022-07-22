#!/usr/bin/python3
# -*- coding: utf-8 -*-


class Singleton:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            print("__new__ is called\n")
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        cls = type(self)
        if not hasattr(cls, "_init"):
            print("__init__ is called\n")
            cls._init = True
            self.test_class = TestClass()


class TestClass:
    def __init__(self):
        self.a = 1
        self.b = 2
        self.c = 3


def main():
    Singleton()
    Singleton()
#    s1 = Singleton()
#    s2 = Singleton()
#    print(f"s1's id :: {id(s1)}")
#    print(f"s2's id :: {id(s2)}")
#
#    print(f"s1's TestClass instance id :: {id(s1.test_class)}")
#    print(f"s2's TestClass instance id :: {id(s2.test_class)}")

if __name__ == '__main__':
    main()
