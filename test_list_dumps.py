#!/usr/bin/python3
# -*- coding: utf-8 -*-

import json


class Test:

    def __init__(self): pass

    def convertToStr(self, data):
        return json.dumps(data)


def main():
    test_data = [{"test1":1}]
    t = Test()
    print(f"t.convertToStr(test_data) :: {t.convertToStr(test_data)}")
    print(f"type(t.convertToStr(test_data)) :: {type(t.convertToStr(test_data))}")


if __name__ == "__main__":
    main()
