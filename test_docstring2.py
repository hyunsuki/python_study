#!/usr/bin/python3
# -*- coding: utf-8 -*-


class Test:
    def __init__(self): pass

    def testMethod(self):
        '''
        This is test method
        '''


def main():
    t = Test()
    print(t.testMethod.__doc__)


if __name__ == '__main__':
    main()
