#!/usr/bin/python3
# -*- coding: utf-8 -*-

import random
from enum import Enum


class CustomEnum(Enum):
    @classmethod
    def getRandomValue(cls):
        members = list(cls.__members__.values())
        if len(members) != 0:
            return random.choice(members)


class TestEnum(CustomEnum): pass
    TEST1 = 0
    TEST2 = 1
    TEST3 = 2
    TEST4 = 3
    TEST5 = 4
    TEST6 = 5


def main():
    num = 100
    for i in range(1, num):
        print(f"{i} :: {TestEnum.getRandomValue()}")


if __name__ == '__main__':
    main()
