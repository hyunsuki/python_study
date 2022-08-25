#!/usr/bin/python3
# -*- coding: utf-8 -*-

import numpy as np
import random
from enum import Enum
from enum import EnumMeta


class Test(Enum):
    NAVER_SMART = 0
    GOOGLE = 1
    COM_NAVER_WHALE = 2
    COM_ANDROID_CHROME = 3
    APPSRANK = 4


class Vo:
    def __init__(self, a, b, c, d, e):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e


class Utils:

    def __init__(self, data):
        self.data = data
        self.weights = Weights()
        self.__setRandomWeights()
        print(f"probabilltys :: {self.weights.probabilltys}")

    def getRandom(self):
        return str(np.random.choice(self.getList(), 1, p=self.weights.probabilltys)[0])

    def getList(self):
        if isinstance(self.data, EnumMeta): return [member.name for member in self.data]
        elif isinstance(self.data, object): return [key for key in list(self.data.__dict__.values())]
        else: return None

    def getLen(self):
        if isinstance(self.data, EnumMeta): return len(self.data)
        elif isinstance(self.data, object): return len(self.data.__dict__)
        else: return None

    def __setRandomWeights(self):
        p = 1.0
        for i in range(self.getLen()):
            # 마지막 실행
            if i == self.getLen()-1: rand_p = p
            else: rand_p = random.uniform(0, p)
            self.weights.probabilltys.append(rand_p)
            p = p-rand_p


class Weights:

    def __init__(self):
        self.probabilltys = []


def main():
#    test_data = Vo(1, 2, 3, 4, 5)
    test_data = Test
    

    num = 100000

    u = Utils(test_data)
    print(f"u.getRandom() :: {u.getRandom()}")
    print(f"type(u.getRandom()) :: {type(u.getRandom())}")

#    result = []
#    for i in range(0, num):
#        result.append(u.getRandom())
#
#    print(f"type(u.getList()) :: {type(u.getList())}")
#    for param in u.getList():
#        print(f"{param} 확률 :: {result.count(param)/num}")


if __name__ == "__main__":
    main()
