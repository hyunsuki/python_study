#!/usr/bin/python3
# -*- coding: utf-8 -*-


class SuperClass:
    def __init__(self):
        self.a = 0
        self.b = 1
        self.c = 2

    def getattrs(self):
        return self.__dict__


class TestClass(SuperClass):
    def __init__(self):
#        super(TestClass, self).__init__()
        super().__init__()
        self.d = 3
        self.e = 4
        self.f = 5

#    def getattrs(self):
#        for instance_value in super().__dict__:
#            setattr(self, instance_value, super().__dict__[instance_value])

#        return self.__dict__


def main():
    s = SuperClass()
    t = TestClass()
    print(f"s.getattrs() :: {s.getattrs()}")
    print(f"t.getattrs() :: {t.getattrs()}")


if __name__ == '__main__':
    main()
