#!/usr/bin/python3
#-*- coding: utf-8 -*-


class Singleton:
   def __new__(self):
       if not hasattr(cls, "_instance"): pass
   def __init__(self): pass


class TestClass:
   def __init__(self): pass


def main():
    tc = TestClass()
    print(tc._instance)


if __name__ == '__main__':
    main()
