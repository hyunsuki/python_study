#!/usr/bin/python3
# -*- coding: utf-8 -*-


class Test:

    def __init__(self): pass

    def test(self, a=None, b=None, c=''):
        print(f"a :: {a}")
        print(f"b :: {b}")
        print(f"c :: {c}")


def main():
    t = Test()
    print("t.test()")
    t.test()
    print("\nt.test(1, 2, 3)")
    t.test(1, 2, 3)
    print("\nt.test(a=3, b=2, c=1)")
    t.test(a=3, b=2, c=1)
    print("\nt.test(a=1)")
    t.test(a=1)
    print("\nt.test(1)")
    t.test(1)


if __name__ == "__main__":
    main()
