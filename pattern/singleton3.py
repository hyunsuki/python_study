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


def main():
    s1 = Singleton()
    s2 = Singleton()
    print(f"s1's id :: {id(s1)}")
    print(f"s2's id :: {id(s2)}")


if __name__ == '__main__':
    main()
