#!/usr/bin/python3
# -*- coding: utf-8 -*-
from test_singleton import Singleton

class TestClass(Singleton):

    @classmethod
    def get(self):
        return 'abc'


def main():
    tc1 = TestClass.get_instance()
    tc2 = TestClass.get_instance()
    print(id(tc1) == id(tc2))
    print(TestClass.get())


if __name__ == '__main__':
    main()
