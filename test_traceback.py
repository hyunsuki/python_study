#!/usr/bin/python3
# -*- coding: utf-8 -*-

import traceback


class TestClass:

    def __init__(self):
        self.num = 10

    def doWhat(self, num):
        try:
            result = self.num / num
            return result
        except:
            error_message = traceback.format_exc()
            print(f"error_message type :: {type(error_message)}")
            print(f"error_message :: {error_message}")


def main():
    tc = TestClass()
    tc.doWhat(0)


if __name__ == '__main__':
    main()
