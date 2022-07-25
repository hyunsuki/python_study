#!/usr/bin/python3
# -*- conding: utf-8 -*-

from threading import Lock
 

class Singleton:
    __instance = None
    __lock = Lock()

    @classmethod
    def getInstance(cls, *args, **kwargs):
        print(f"cls :: {cls}")
        print(f"cls.__new__ :: {cls.__new__}")
        print(f"super().__new__(cls) :: {super().__new__(cls)}")
        with cls.__lock:
            if cls.__instance is None:
                cls.__instance = cls(*args, **kwargs)
        return cls.__instance


class TestClass(Singleton):

    @classmethod
    def sayWord(self, word):
        print(f'{word}')


class TestClass2:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            print("__new__ is called\n")
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        cls = type(self)
        print(id(super().__new__(cls)))
        if not hasattr(cls, "_init"):
            print("__init__ is called\n")
            cls._init = True
            self.test_class = TestClass()


def main():
    tc1_1 = TestClass.getInstance()
    tc1_2 = TestClass.getInstance()
    print(f'id(tc1_1) == id(tc1_2) => {id(tc1_1) == id(tc1_2)}')

    tc2_1 = TestClass2()
    tc2_2 = TestClass2()
    print(f"tc2_1's id :: {id(tc2_1)}")
    print(f'id(tc2_1) == id(tc2_2) => {id(tc2_1) == id(tc2_2)}')

    # test
    TestClass.sayWord('Hello')

if __name__ == '__main__':
    main()
