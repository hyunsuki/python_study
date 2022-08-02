#!/usr/bin/python3
# -*- coding: utf-8 -*-

from inspect import signature


class SuperClass:
    def __init__(self):
        self.a = 0
        self.b = 1
        self.c = 2

    def getAttrs(self):
        return self.__dict__

    def setAttrs(self, **kwargs):
        for input_key in kwargs.keys():
            self.setting(input_key, **kwargs)

    def setting(self, input_key, **kwargs):
        if input_key in self.__dict__:
            print(f"input_key :: {input_key}")
            print(f"input_key's value :: {kwargs.get(input_key)}")
            setattr(self, input_key, kwargs.get(input_key))



class TestClass(SuperClass):
    def __init__(self):
        super().__init__()
        self.d = 3
        self.e = 4
        self.f = 5

    def test(self, a, b, c):
        print(dir(self.test))
        print(self.test.__get__)
        


def main():
    test_dict = {'f': 10}
    s = SuperClass()
    t = TestClass()
    print(f"s.getAttrs() :: {s.getAttrs()}")
    print(f"t.getAttrs() :: {t.getAttrs()}")

    t.setAttrs(**test_dict)
    print(f"t.getAttrs() :: {t.getAttrs()}")

    t.test(1, 2, 3) 


if __name__ == '__main__':
    main()
