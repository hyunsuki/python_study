#!/usr/bin/python3
# -*- coding: utf-8 -*-


class Test:
    def __init__(self):
        cls = type(self)
        print(f'cls :: {cls}')
        if not hasattr(cls, "_init"):
            print("__init__ is called\n")
            cls._init = True
            print(f"cls._init :: {cls._init}")

    @classmethod
    def printDir(self, value):
        print(dir(value))


def main():
    test = Test()
    Test.printDir(Test)
    Test.printDir(object)
    print(f"\nobject.__dict__ :: {object.__dict__}")

    print(hasattr(Test, "__class__"))
    print(hasattr(Test, "_init"))
    print(hasattr(test, "_init"))

if __name__ == '__main__':
    main()
