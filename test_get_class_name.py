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


class CustomEunm(Enum):
    @classmethod
    def getName(cls):
#        return dir(cls.__class__)
        return cls.__class__.__members__


class TestEnumClass(Enum):
    Test1 = 'test1'
    Test2 = 'test2'

    def getClsName():
        return TestEnumClass.Test1.__class__.__name__


def main():
    print(TestEnumClass.getClsName())



if __name__ == '__main__':
    main()
