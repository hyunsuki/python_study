#!/usr/bin/python3
# -*- coding: utf-8 -*-


class Base:
    __slots__ = 'foo', 'bar'


def main(): print(f"Base.__slots__ :: {Base.__slots__}")


if __name__ == '__main__':
    main()
