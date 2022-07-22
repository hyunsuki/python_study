#!/usr/bin/python3
# -*- conding: utf-8 -*-


class Point:
    def __new__(cls, *args, **kwargs):
        print("\nPoint.__new__ called")
        print(f"cls :: {cls}")
        print(f"args :: {args}")
        print(f"kwargs :: {kwargs}")
        obj = super().__new__(cls)
        obj.args = args
        obj.kwargs = kwargs
        return obj

    def __init__(self, x=0, y=0):
        print("\nPoint.__init__ called")
        print(f"args :: {self.args}")
        print(f"kwargs :: {self.kwargs}")
        self.x = x
        self.y = y
        print(f"self.x :: {self.x}")
        print(f"self.y :: {self.y}")


class RectPoint(Point):
    MAX_INSTANCE_NUM = 4
    created_instance_num = 0

    def __new__(cls, *args, **kwargs):
        if cls.created_instance_num >= cls.MAX_INSTANCE_NUM:
            raise ValueError("Can not create more object")
        cls.created_instance_num += 1
        return super().__new__(cls)


def main():
    point1 = RectPoint(0, 0)
    point2 = RectPoint(1, 0)
    point3 = RectPoint(1, 1)
    point4 = RectPoint(0, 1)

    point5 = RectPoint(2, 2)

if __name__ == '__main__':
    main()
