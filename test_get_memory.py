#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys


class MemoryManager:
    def __init__(self): pass

    def getMemory(self, object_):
        return sys.getsizeof(object_)


def main():
    test_data1 = {'test1': 1, 'test2': 2, 'test3': 3}
    test_data2 = {'test1': 1, 'test2': 2, 'test3': 3, 'test4': 4}
    mm = MemoryManager()
    print(f'mm.getMemory(test_data1) :: {mm.getMemory(test_data1)}')
    print(f'mm.getMemory(test_data2) :: {mm.getMemory(test_data2)}')

    # get_asyncgen_hooks
    print(f"hasattr(sys, 'get_asyncgen_hooks') :: {hasattr(sys, 'get_asyncgen_hooks')}")


if __name__ == "__main__":
    main()
