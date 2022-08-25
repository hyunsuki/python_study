#!/usr/bin/python3
# -*- coding: utf-8 -*-

from enum import Enum
from enum import EnumMeta


class TestEnum(Enum):
    TEST1 = 0
    TEST2 = 1
    TEST3 = 2
    TEST4 = 3


def main():
    print(f"type(TestEnum :: {type(TestEnum)})")
    print(f"isinstance(TestEnum, EnumMeta) :: {isinstance(TestEnum, EnumMeta)}")

if __name__ == '__main__':
    main()
