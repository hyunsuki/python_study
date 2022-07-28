#!/usr/bin/python3
# -*- coding: utf-8 -*-


class Test:
    def __init__(self, var):
        self.var = var or None

    def getVar(self):
        return self.var


def main():
    t1 = Test(1)
    t2 = Test(None)
    t3 = IndexError

    print(f"t1.getVar() :: {t1.getVar()}")
    print(f"t2.getVar() :: {t2.getVar()}")
    print(t3)


if __name__ == '__main__':
    main()
