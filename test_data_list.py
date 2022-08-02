#!/usr/bin/python3
# -*- coding: utf-8 -*-


class Test:
    def __init__(
          self
        , param_a=None
        , param_b=None
        , param_c=None
    ):
        self.param_a = param_a
        self.param_b = param_b
        self.param_c = param_c

    def getParams(self):
        return self.__dict__


def main():
    test_list = []
    test = Test("param_a", "param_b", "param_c")
    test_list.append(test.getParams())
    print(f"test_list :: {test_list}")


if __name__ == '__main__':
    main()
