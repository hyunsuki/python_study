#!/usr/bi/python3
# -*- coding: utf-8 -*-

from memory_profiler import profile


f = open('memory.dat', "w+")


@profile(stream=f)
def my_func():
    a = [1] * (10 ** 6)
    b = [2] * (2 * 10 ** 7)
    del b
    return a

if __name__ == '__main__':
    my_func()
