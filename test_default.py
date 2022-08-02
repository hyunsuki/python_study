#!/usr/bin/python3
# -*- coding: utf-8 -*-


class Test:
    def __init__(self):
        self.param1 = None
        self.param2 = None
        self.param3 = None

    def test(self, param1, param2, param3='param3'):
        self.param1 = param1
        self.param2 = param2
        self.param3 = param3


def main():
    t = Test()
    t.test('param1', 'param2', 'error')
    print(f"Test.param1 :: {t.param1}")
    print(f"Test.param2 :: {t.param2}")
    print(f"Test.param3 :: {t.param3}")


if __name__ == '__main__':
    main()
