#!/usr/bin/python3
# -*- coding: utf-8 -*-

import json
from enum import Enum


class JsonManager:
    def __init__(self, data_dict):
        self.__data_dict = data_dict

    def getDataDict(self):
        return self.__data_dict

    def convertDictToJson(self):
        self.__data_dict = json.dumps([self.__data_dict])

class Value:
    def __init__(self): pass

    def setValue(self, argu, default): # argu is enum member
        return default if argu is None or argu == "" else argu


class Test(Enum):
    TEST1 = 0
    TEST2 = 1
    TEST3 = 2


def main():
    test1 = ''
    test2 = None
    test3 = 'test3'

    test_data = {}
    v = Value()
    test_data.setdefault(
          Test.TEST1.name
        , v.setValue(test1, 'test1_default')
    )
    test_data.setdefault(
          Test.TEST2.name
        , v.setValue(test2, 'test2_default')
    )
    test_data.setdefault(
          Test.TEST3.name
        , v.setValue(test3, 'test3_default')
    )
    print(f"test_data :: {test_data}")
    print(f"[test_data] :: {[test_data]}")
    j = JsonManager(test_data)
    j.convertDictToJson()
    print(f"j.getDataDict() :: {j.getDataDict()}")
    print(f"type(j.getDataDict()) :: {type(j.getDataDict())}")


if __name__ == "__main__":
    main()
