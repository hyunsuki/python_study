#!/usr/bin/python3
# -*- coding: utf-8 -*-

from enum import Enum


class Test1:
    def __init__(self):
        self.value = None


class Test2:
    def __init__(self):
        self.value = None


class Test3:
    def __init__(self):
        self.value = None


class Test4:
    def __init__(self):
        self.value = None


class TestEnum(Enum):
    TEST1 = Test1
    TEST2 = Test2
    TEST3 = Test3
    TEST4 = Test4


def main():
    print(f"Test1's value :: {TestEnum.TEST1.value.value}")
    print(f"Test2's value :: {TestEnum.TEST2.value.value}")
    print(f"Test3's value :: {TestEnum.TEST3.value.value}")
    print(f"Test4's value :: {TestEnum.TEST4.value.value}")

#    print(f"Test1's type :: {type(TestEnum.Test1)}")
#    print(f"Test2's type :: {type(TestEnum.Test2)}")
#    print(f"Test3's type :: {type(TestEnum.Test3)}")
#    print(f"Test4's type :: {type(TestEnum.Test4)}")

if __name__ == '__main__':
    main()
