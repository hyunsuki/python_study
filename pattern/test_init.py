#!/usr/bin/python3
# -*- coding: utf-8 -*-


from singleton_init_test import Test


class Init:
    def __init__(self):
        self.test = Test()

    def init(self):
        self.test.initTest()


def main():
    init1 = Init()
    init2 = Init()
    print(f"init1.test's id :: {id(init1.test)}")
    print(f"init2.test's id :: {id(init2.test)}")
    init1.test.initTest(only_init=False)
    init3 = Init()
    print(f"init3.test's id :: {id(init3.test)}")


if __name__ == '__main__':
    main()
