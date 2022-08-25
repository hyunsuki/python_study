#!/usr/bin/python3
# -*- coding: utf-8 -*-


class Test:
    def __init__(self): pass

    def test(self, param1, param2=None, param3=''):
        self.param1 = param1
        self.param2 = 'param2 default' if param2 is None or param2 == '' else param2
        self.param3 = 'param3 default' if param3 is None or param3 == '' else param3


def main():
    t = Test()
    t.test('param1')
    
    print(f"Test.param1 :: {t.param1}")
    print(f"Test.param2 :: {t.param2}")
    print(f"Test.param3 :: {t.param3}")


if __name__ == '__main__':
    main()
