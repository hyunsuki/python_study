#!/usr/bin/python3
# -*- coding: utf-8 -*-

from enum import Enum


class TestClass:
    def __init__(self):
        pass

    def getNameUseType(self):
        return type(self).__name__

    def getNameUseClass(self):
        return self.__class__.__name__


class CustomEnum(Enum):
    @classmethod
    def getClsName(cls):
        return list(cls.__members__.values())[0].__class__.__name__


class TestEnumClass(CustomEnum):
    Test1 = 'test1'
    Test2 = 'test2'


def main():
    print(TestEnumClass.getClsName())



if __name__ == '__main__':
    main()
