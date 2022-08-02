#!/usr/bin/python3
# -*- coding: utf-8 -*-

from enum import Enum


class Test(Enum):
    TEST1 = 0
    TEST2 = 1
    TEST3 = 2

    def get(param):
        if isinstance(param, str):
            print(param if param.isupper() else param.upper())
            return Test[param if param.isupper() else param.upper()]

        if isinstance(param, int):
            return Test(param)


def main():
#    print(f"Test.__members__ type :: {Test.__members__}")
#    print(Test.TEST1 in Test.__members__.values())
#    print(f"Test.TEST1.name :: {Test.TEST1.name}")
#
#    print(f"Test(0) :: {Test(0)}")
#    print(f"Test['TEST1'] :: {Test['TEST1']}")

    print(f"Test.get('TEST1') :: {Test.get('TEST1')}")
    print(f"Test.get('test1') :: {Test.get('test1')}")


if __name__ == '__main__':
    main()
