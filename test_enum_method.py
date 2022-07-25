#!/usr/bin/python3
# -*- coding: utf-8 -*-

from enum import Enum


# Custom Enum 
class CEnum(Enum):
    def __init__(self, value):
        self.value = value

    @classmethod
    def getClsName(cls):
#        return cls.__class__.__name__
        return type(cls).__name__


class Test(CEnum):
    TEST1 = 'test1'
    TEST2 = 'test2'
    TEST3 = 'test3'


def main():
    t = Test()
    print(t.getClsName())


if __name__ == '__main__':
    main()
