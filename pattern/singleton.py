#!/usr/bin/python3
# -*- conding: utf-8 -*-


class Singleton:
    __instance = None

    def __init__(self):
        print('Instance exist yet')

    @classmethod
    def getInstance(cls, *args, **kwargs):
        cls.__instance = cls.__instance or cls(*args, **kwargs)
        return cls.__instance


class TestClass(Singleton):

    def __init__(self):
        Singleton.__init__(self)

    @classmethod
    def sayWord(self, word):
        print(f'{word}')

    @classmethod
    def get(self):
        return SubSystem.getPid() 

class SubSystem:

    @classmethod
    def getPid(self):
        with open('test.pid', mode='r') as f:
            return f.readline()


def main():
    tc1 = TestClass.getInstance()
    tc2 = TestClass.getInstance()
    print(f'id(tc1) == id(tc2) => {id(tc1) == id(tc2)}')

    # test
    TestClass.sayWord('Hello')
    print(TestClass.get())


if __name__ == '__main__':
    main()
